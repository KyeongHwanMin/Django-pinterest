from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form): #forms.py에 있는 form을 받음
        temp_profile = form.save(commit=False) #임시 저장 이므로 commit=False(임시데이터 저장 DB저장 x)
        temp_profile.user = self.request.user
        temp_profile.save()

        return super().form_valid(form)
