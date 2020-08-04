from django.shortcuts import render
from django.utils import timezone
from my_app.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.

# renders the home page
def home(request):
	todo_items= Todo.objects.all().order_by("-added_date")

	staff_of_the_frontend= {
	   'todo_items': todo_items,
	      }

	return render(request, 'my_app/index.html', staff_of_the_frontend)


# captures the dataand saves it
def add_todo(request):
	# this registers the data to the model
	current_date= timezone.now()
	content=request.POST.get('content')

	# now saving the data to the database
	created_obj=Todo.objects.create( added_date= current_date, text= content)

	
	
	return HttpResponseRedirect('/')



# to delete the todo_items

def delete_todo(request, todo_id):
	Todo.objects.get(id =todo_id).delete()

	return HttpResponseRedirect('/')





