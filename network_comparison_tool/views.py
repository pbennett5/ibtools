# views.py
from django.shortcuts import render
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


# views.py
from .utils import identify_insurance_company, import_data_to_db

def handle_uploaded_file(file):
    # Read the Excel file using pandas
    df = pd.read_excel(file, engine='openpyxl')

    # Identify the insurance company based on headers
    insurance_company = identify_insurance_company(df.columns)

    # Import data into the MySQL database
    import_data_to_db(df, insurance_company)
