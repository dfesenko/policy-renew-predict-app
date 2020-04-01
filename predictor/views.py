from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

from .forms import UploadFileForm
from .utils import predict, load_model_and_train_cols


class IndexView(View):
    classifier, train_cols = load_model_and_train_cols()

    def get(self, request):
        upload_file_form = UploadFileForm()
        return render(request, 'predictor/index.html', {'upload_file_form': upload_file_form})

    def post(self, request):
        upload_file_form = UploadFileForm(request.POST, request.FILES)

        if upload_file_form.is_valid():
            file = request.FILES['file']

            result_df = predict(file, self.classifier, self.train_cols)

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="result.csv"'
            result_df.to_csv(response, sep=';', index=False)
            return response
