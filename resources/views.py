
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course,Resource
from .serializers import CourseSerializer,ResourceSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator



@api_view(['GET'])
def course_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

# Create your views here.

@api_view(['GET'])
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    serializer = CourseSerializer(course)
    return Response(serializer.data)


@api_view(['POST'])
def course_create(request):
    serializer = CourseSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    serializer = CourseSerializer(course, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return Response(status=204)


@api_view(['GET'])
def resource_list(request):
    resources = Resource.objects.all()
    paginator = Paginator(resources, 2)

    page_number = request.query_params.get('page', '1')

    if not page_number.isdigit() or int(page_number) < 1:
        return Response(
            {'error': 'Page must be a positive number.'},
            status=400
        )

    resources_page = paginator.get_page(page_number)
    serializer = ResourceSerializer(resources_page, many=True)

    return Response({
        'total_resources': paginator.count,
        'total_pages': paginator.num_pages,
        'current_page': resources_page.number,
        'results': serializer.data
    })




@api_view(['GET'])
def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    serializer = ResourceSerializer(resource)
    return Response(serializer.data)


@api_view(['POST'])
def resource_create(request):
    serializer = ResourceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def resource_update(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    serializer = ResourceSerializer(
        resource,
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def resource_delete(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    resource.delete()
    return Response(status=204)


@api_view(['GET'])
def course_resources(request, pk):
    course = get_object_or_404(Course, pk=pk)
    resources = Resource.objects.filter(course=course)
    serializer = ResourceSerializer(resources, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def course_resource_counts(request):
    courses = Course.objects.annotate(
        resource_count=Count('resources')
    )
    serializer = CourseSerializer(courses, many=True)
    data = serializer.data

    for course_data, course in zip(data, courses):
        course_data['resource_count'] = course.resource_count

    return Response(data)

