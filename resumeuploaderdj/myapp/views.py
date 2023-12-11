from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View
import os
import nltk
import string
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from django.views import View

# Ensure that NLTK resources are downloaded (run once)
nltk.download('punkt')
nltk.download('stopwords')

class HomeView(View):
 def get(self, request):
  form = ResumeForm()
  candidates = Resume.objects.all()
  return render(request, 'myapp/home.html', { 'candidates':candidates, 'form':form})

 def post(self, request):
  form = ResumeForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return render(request, 'myapp/home.html', {'form':form})

class CandidateView(View):
 def get(self, request, pk):
  candidate = Resume.objects.get(pk=pk)
  return render(request, 'myapp/candidate.html', {'candidate':candidate})

class ResumeAnalysisView(View):
    def get(self, request):
        # Define the path to the resume file
        resume_file_path = r'C:\Users\alwyn\OneDrive\Desktop\Project\resumeuploaderdj\media\doc\resume2.txt'

        # Read the content of the resume file
        with open(resume_file_path, 'r', encoding='utf-8') as file:
            resume_content = file.read()

        # Tokenize the words
        words = word_tokenize(resume_content)

        # Remove stopwords, punctuation, and convert to lowercase
        stop_words = set(stopwords.words('english'))
        words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

        # Create a frequency distribution
        freq_dist = FreqDist(words)

        # Plot a bar chart using Seaborn
        plt.figure(figsize=(10, 6))
        sns.barplot(x=list(freq_dist.keys())[:10], y=list(freq_dist.values())[:10], palette="viridis")
        plt.title("Top 10 Most Frequent Words in Resume")
        plt.xlabel("Words")
        plt.ylabel("Frequency")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot to a file or display it
        plot_path = os.path.join(os.path.dirname(resume_file_path), 'word_frequency_plot.png')
        plt.savefig(plot_path)
        plt.show()

        # Categorize the resume into its professional domain
        professions = ['data analyst', 'database developer', 'software engineer', 'dancer', 'lawyer', 'accountant', 'manager']

        # Calculate the maximum iterated word
        max_word = max(freq_dist, key=freq_dist.get)

        # Categorize the resume based on the maximum iterated word
        if max_word in professions:
            professional_domain = max_word
        else:
            professional_domain = 'Database Developer'

        return render(request, 'myapp/plot.html', context={'plot_path': plot_path, 'professional_domain': professional_domain})
    
class AboutUsView(View):
    def get(self, request):
        return render(request, 'myapp/aboutus.html')