from django.test import TestCase
from views import hist_generation,line_generation,box_generation,pie_generation

# Create your tests here.
def hist_graph_test():
    hist_generation()

def line_graph_test():
    line_generation()

def box_graph_test():
    box_generation()

def pie_graph_test():
    pie_generation()
if __name__ == '__main__':
    pie_graph_test()
