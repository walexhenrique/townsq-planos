from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from .forms import AttendanceForm


class planosView(View):
    def get(self, request):
        form = AttendanceForm(self.request.session.get('attendance'))
        return render(self.request, 'planos/planos.html', {'form': form})
    
    def post(self, request):
        POST = request.POST
        form = AttendanceForm(request.POST)
        self.request.session['attendance'] = POST

        if form.is_valid():
            form.save()
            del self.request.session['attendance']
            messages.success(self.request, 'Solicitação enviada com sucesso!')
            return redirect('planos:planos')
        
        return redirect('planos:planos')