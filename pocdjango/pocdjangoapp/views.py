from django.shortcuts import redirect, render
from django.views import View, generic
import rpy2.robjects as robjects

class DashboardView(generic.TemplateView):
    template_name = "pocdjangoapp/dashboard.html"

class GenerateFromFileView(View):
    def post(self, request):
        if request.FILES['panel']:
            panel = request.FILES['panel']

            file_target = "pocdjangoapp/Rscript/test.R"

            ro=robjects.r        
            ro.source(file_target)
            res = ro.func(12)

        return redirect('dashboard')