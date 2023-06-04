from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import Student, Track
from .forms import StudentForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils.timezone import now
from .serializers import StudentSerializer


# ________________________________________________ FUNCTION BASED VIEWS _______________
# def index(request):
#     context = {}
#     try:
#         all_students = Student.objects.all()
#         context = {'students': all_students}
#     except Exception as e:
#         print(f'exception in e_learning/index => {e}')
#     return render(request, 'e_learning/index.html', context)


# def add_student(request):
#     student_form = StudentForm()
#     try:
#         if request.method == 'POST':
#             student_form = StudentForm(request.POST)
#             # form = BookForm(request.POST or None, request.FILES or None)
#             if student_form.is_valid():
#                 student_form.save()
#                 return redirect('index')
#     except Exception as e:
#         print(f'exception in add_student => {e}')
#     return render(request, 'e_learning/add_student.html', {'student_form': student_form})
#
# def edit_student(request, id):
#     student_form = StudentForm()
#     try:
#         student = get_object_or_404(Student, id=id)
#         if request.method == 'POST':
#             student_form = StudentForm(request.POST, instance=student)
#             # form = BookForm(request.POST or None, request.FILES or None, instance=book)
#             if student_form.is_valid():
#                 student_form.save()
#                 return HttpResponseRedirect('/')
#
#         student_form = StudentForm(instance=student)
#     except Exception as e:
#         print(f'exception in edit_student => {e}')
#     return render(request, 'e_learning/add_student.html', {'student_form': student_form})
#
#
# def delete_student(request, id):
#     try:
#         student = get_object_or_404(Student, id=id)
#         student.delete()
#     except Exception as e:
#         print(f'exception in delete_student => {e}')
#     return redirect(reverse('index'))


# ________________________________________________ CLASS BASED VIEWS _______________

class StudentList(generic.ListView):
    model = Student
    template_name = 'e_learning/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        from datetime import datetime
        context = super().get_context_data()
        context['today'] = datetime.now()
        return context


class StudentDetail(generic.DetailView):
    model = Student
    template_name = 'e_learning/student_detail.html'


class StudentCreate(generic.CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'e_learning/add_student.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.Student_reg_date = now()
        return super().form_valid(form)


class StudentUpdate(generic.UpdateView):
    model = Student
    template_name = 'e_learning/add_student.html'
    form_class = StudentForm
    success_url = reverse_lazy('index')

class StudentDelete(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

#_________________________________________________ REST FRAMEWORK ________________________


@api_view(['GET'])
def get_all_students_api(request):
    data = {}
    try:
        students = Student.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        data = students_serializer.data
        http_status = status.HTTP_200_OK
    except Exception as e:
        print(f'exception in get_all_student_api => {e}')
        http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    return Response(data=data, status=http_status)

@api_view(['POST'])
def add_student_api(request):
    data = {}
    try:
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            data = student.data
            http_status = status.HTTP_201_CREATED
    except Exception as e:
        print(f'exception in create api => {e}')
        http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    return Response(data=data, status=http_status)


@api_view(['GET', 'PUT', 'DELETE'])
def one_student(request, id):
    data = {}

    try:
        student = get_object_or_404(Student, id=id)
        if request.method == 'GET':
            student_serializer = StudentSerializer(instance=student)
            data = student_serializer.data
            http_status = status.HTTP_200_OK
        # fixme: check why it is not updating one field only!
        if request.method == 'PUT':
            student_serializer = StudentSerializer(instance=student, data=request.data)
            if student_serializer.is_valid():
                student_serializer.save()
                data = student_serializer.data
                http_status = status.HTTP_200_OK
        if request.method == 'DELETE':
            student.delete()
            http_status = status.HTTP_204_NO_CONTENT
    except Exception as e:
        print(f'exception in one student => {e}')
        http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    return Response(data=data, status=http_status)