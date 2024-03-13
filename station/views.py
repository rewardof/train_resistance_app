from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.generics import CreateAPIView

from station.export import export_natural_list_data
from station.models import NaturalList, Vagon
from station.serializers import ProcessNaturalListSerializer
from station.services import NaturalListService


class ProcessNaturalList(CreateAPIView):
    serializer_class = ProcessNaturalListSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data.get('file')
        self.handle_uploaded_file(file)

        natural_list = NaturalList.objects.create(
            name=serializer.validated_data.get('name'),
            code=serializer.validated_data.get('code'),
        )
        processor = NaturalListService(natural_list)
        processor.import_data(file_path=file.name)

        response = export_natural_list_data(
            Vagon.objects.filter(natural_list=natural_list).order_by('order')
        )
        return response

    def handle_uploaded_file(self, file):
        # Ensure file is an InMemoryUploadedFile
        if isinstance(file, InMemoryUploadedFile):
            # Open a new file in memory
            memory_file = BytesIO()

            # Write the contents of the uploaded file to the memory file
            # Open a new file in binary write mode
            with open(file.name, 'wb') as destination:
                # Iterate over chunks and write them to the destination file
                for chunk in file.chunks():
                    destination.write(chunk)

            # Now you have the file object in memory, you can perform operations like reading or processing it
            # For example, you can pass this memory_file object to pyexcel to process the data

            # Return the memory file object
            return memory_file
