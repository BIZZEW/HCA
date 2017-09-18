# from django.http import HttpResponse
# from django.template import loader
# from django.http import Http404
# from django.shortcuts import render, get_object_or_404
# from .models import Album, Song
#
#
# def index(request):
#     all_albums = Album.objects.all()
#     # context = {
#     #     'all_albums': all_albums,
#     # }
#
#     # html = ''
#     # for album in all_albums:
#     #     url = '/health/' + str(album.id) + '/'
#     #     html += '<a href="' + url + '">' + album.album_title + '</a><br>'
#
#     # template = loader.get_template('health/index.html')
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'health/index.html', {'all_albums': all_albums})
#
#
# def detail(request, album_id):
#     # try:
#         # album = Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does not exist")
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'health/detail.html', {'album': album})


# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'health/detail.html', {
#             'album': album,
#             'error_message': "You did not select a valid song",
#         })
#     else:
#         if selected_song.is_favorite:
#             selected_song.is_favorite = False
#         else:
#             selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'health/detail.html', {'album': album})
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Album
from .forms import UserForm


class IndexView(generic.ListView):
    # model = Album
    template_name = 'health/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'health/detail.html'


class AlbumCreate(CreateView, generic.ListView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    context_object_name = 'all_albums'
    success_url = reverse_lazy('health:album-add')


class AlbumUpdate(UpdateView, generic.ListView):
    model = Album
    context_object_name = 'all_albums'
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    success_url = reverse_lazy('health:album-add')


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('health:album-add')


class UserFormView(View):
    form_class = UserForm
    template_name = 'health/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('health:index')

        return render(request, self.template_name, {'form': form})
