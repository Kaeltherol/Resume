import matplotlib.pyplot as plt

x = 1
y = 0
#set colors
body_color = '#000000'
#headers_color = '#58C1B2'
headers_color = '#00008b'
# Text Variables

#defining lines as a superclass named Block, with line types with their attributes as child classes

class Block:

  def __init__(self, str_txt: str):
    self.txt = str_txt
    self.posx = 0.0
    self.posy = 0.0
    self.weight = 'regular'
    self.color = '#000000'
    self.size = 10-y
    self.alpha = 1
    self.prev = None
    self.dist = 0.02
    self.xshift = 0.0
    self.yshift = 0.0


  def __annotate__(self):
    plt.annotate(self.txt, (self.posx,self.posy), weight= self.weight, fontsize=self.size, alpha = self.alpha, color = self.color)

class Header(Block):

  def __init__(self, txt_str: str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.color = headers_color
    self.size = 12*mltply-y
    self.alpha = 1
    self.dist = 0.025

class Top_Header(Block):

  def __init__(self, txt_str: str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.color = '#000000'
    self.size = 10*mltply-y
    self.alpha = 0.5
    self.dist = 0.035

class Name(Block):

  def __init__(self, txt_str: str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.color = '#000000'
    self.size = 20*mltply-y
    self.alpha = 1
    self.dist = 0.017

class Info(Block):

  def __init__(self, txt_str: str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'regular'
    self.color = '#000000'
    self.size = 20*mltply-y
    self.alpha = 1

class Lateral(Block):

  def __init__(self, txt_str: str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'regular'
    self.size = 9*mltply-y
    self.alpha = 1
    self.color = '#ffffff'

class Lateral_header(Block):

  def __init__(self, txt_str: str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.size = 13*mltply-y
    self.alpha = 1
    self.color = '#ffffff'
    self.dist = 0.025

class Lateral_title(Block):

  def __init__(self, txt_str: str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.size = 11*mltply-y
    self.alpha = 1
    self.color = '#ffffff'
    self.dist = 0.025

class Lateral_info(Block):

  def __init__(self, txt_str: str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.size = 9.5*mltply-y
    self.alpha = 1
    self.color = '#ffffff'
    self.dist = 0.025       

class Title(Block):

  def __init__(self, txt_str: str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.size = 10*mltply-y
    self.alpha = 1
    self.dist = 0.025
    self.yshift = 0.005

class Place(Block):

  def __init__(self, txt_str: str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.size = 9.5*mltply-y
    self.alpha = 1
    self.dist = 0.025

class Descr(Block):

  def __init__(self, txt_str: str, mltply = 1):
    Block.__init__(self, txt_str)
    self.size = 9*mltply-y
    self.alpha = 1
    self.dist = 0.025

class Time(Block):

  def __init__(self, txt_str: str, mltply = 1):
    Block.__init__(self, txt_str)
    self.xshift = .55
    self.yshift = -.025
    self.size = 9*mltply-y
    self.alpha = 0.6
    self.dist = 0.025

#defining the class train as a succession of lines with structure similar to a linked array

class Train:

  def __init__(self,*args: Block):
    self.blocks = [arg for arg in args]
    for i in range(1,len(self.blocks)):
      self.blocks[i].prev = self.blocks[i-1]

#the class paragraph make possible to print the Train in the chosen position

class Paragraph:
  
  def __init__(self, tuple_pos: float, train: Train):
    train.blocks[0].posx = tuple_pos[0]
    train.blocks[0].posy = tuple_pos[1]
    train.blocks[0].__annotate__()
    self.head = train.blocks[0]
    for i in range(1,len(train.blocks)):
      train.blocks[i].prev = train.blocks[i-1]
      train.blocks[i].posx = self.head.posx + train.blocks[i].xshift
      train.blocks[i].posy = train.blocks[i].prev.posy - train.blocks[i].prev.dist - train.blocks[i].yshift
      train.blocks[i].__annotate__() 
    self.tail = train.blocks[-1]



#set font
plt.rcParams['font.family'] = 'Sans-serif'
plt.rcParams['font.sans-serif'] = 'Calibri'

# Text Variables
#infos
Header1 = Top_Header(' Resume made in Python - Code in my portfolio',mltply = x)
Name1 = Name('NOME COGNOME',mltply = x)
Pers1 = Descr('Birth: 01/01/1990 Birthplace, Birthcountry',mltply = x)
Title1 = Title('Title line1\nTitle line2\nTitle line3',mltply = x)

Info1 = Lateral_header('Contact & Info', mltply= x)

Contact = Lateral_header('Contact', mltply= x)
Contact1 = Lateral_info('\nLocation: Place, PL\nTel: +xx-123456789 \neMail: nomecognome@email.com\n\nMy LinkedIn:\nlinkedin.com/in/nome-cognome\n\nMy Github:\ngithub.com/NomeCognome',mltply = x)

#projects

ProjectsHeader = Header('PROJECTS', mltply = x)

ProjectOneTitle = Title('Improvement of glass vials quality (Pharmaceutical industry)', mltply = x)
ProjectOneDescL1 = Descr('- Analyzed product data to identify the source of defects', mltply = x)

ProjectTwoTitle = Title('Scoring Supplier OTD (On Time Delivery) (Manufacturing industry)', mltply = x)
ProjectTwoDescL1 = Descr('- Assessing suppliers and purchase department performance', mltply = x)


ProjectThreeTitle = Title('Increasing Reach and Impressions on website (Consulting company) ', mltply = x)
ProjectThreeDesc = Descr('- Analyzed Google Analytics Data ', mltply = x)

Portfolio = 'Portfolio website'

#work experience

WorkHeader = Header('WORK EXPERIENCE',mltply = x)

WorkOneTitle = Title('Company Name, Role',mltply = x)
WorkOnePlace = Place('Work Place, Work Country',mltply = x)

WorkOneTime = Time('2018-2020',mltply = x)
WorkOneDescL1 = Descr('- Description line 1;',mltply = x)
WorkOneDescL3 = Descr('- Description line 2',mltply = x)
WorkOneDescL2 = Descr('- Description line 3',mltply = x)

WorkTwoTitle = Title('Company Name, Role',mltply = x)
WorkTwoPlace = Place('Work Place, Work Country',mltply = x)
WorkTwoTime = Time('2015-2018',mltply = x)
WorkTwoDescL1 = Descr('- Description line 1;',mltply = x)
WorkTwoDescL2 = Descr('- Description line 2',mltply = x)
WorkTwoDescL3 = Descr('  Description line 3',mltply = x)


WorkThreeTitle = Title('Company Name, Role',mltply = x)
WorkThreePlace = Place('Work Place, Work Country',mltply = x)
WorkThreeTime = Time('2011-2013',mltply = x)
WorkThreeDesc = Descr('- Description line 1',mltply = x)

#education

EduHeader = Header('EDUCATION',mltply = x)
EduOneTitle = Title('Master\'s degree in Some Faculty',mltply = x) 
EduOnePlace = Place('Some University, Some Country',mltply = x)
EduOneTime = Time('2015',mltply = x)
EduOneDesc1L1 = Descr('- Project Management, Algorithms for Plant Design',mltply = x)
EduOneDesc1L2 = Descr('  Basic Programming skills (C++, Python, Matlab) ',mltply = x)
EduTwoTitle = Title('Lean Six Sigma Black Belt, Some Company',mltply = x)
EduTwoTime = Time('2020',mltply = x)
EduOneDesc2L1 = Descr('- Brainstorming, statistics, FMEA, C&E diagram,',mltply = x)
EduOneDesc2L2 = Descr('  control plans, DOE, Measurement System Analysis',mltply = x)

#skills

SkillsHeader = Lateral_header('Core Skills',mltply=x)
SkillsTitle1 = Lateral_title('Python Skills',mltply =x)
SkillsDesc1L1 = Lateral('- Data Manipulation/Visualization:',mltply =x)
SkillsDesc1L2 = Lateral('   Numpy, Pandas, Matplotlib, Seaborn',mltply =x)
SkillsDesc1L3 = Lateral('   Scipy.',mltply =x)
SkillsDesc1L4 = Lateral('- Web Scraping:',mltply =x)
SkillsDesc1L5 = Lateral('   Selenium, Beautiful Soup.',mltply =x)
SkillsDesc1L6 = Lateral('- Testing:',mltply =x)
SkillsDesc1L7 = Lateral('   Unittest, Pytest, Silk',mltply =x)
SkillsDesc1L8 = Lateral('- Version Control: Git',mltply =x)
SkillsDesc1L10 = Lateral('- Data Structures, Algorithms',mltply =x)
SkillsTitle2 = Lateral_title('Other Skills', mltply=x)
SkillsDesc2L1 = Lateral('- Database Design and Management:',mltply=x)
SkillsDesc2L2 = Lateral('   SQL, MySQL, noSQL',mltply=x)
SkillsDesc2L3 = Lateral('- Probability and Statistics',mltply=x)
SkillsDesc2L4 = Lateral('- Troubleshooting',mltply=x)
SkillsTitle3 = Lateral_title('Soft Skills',mltply=x)
SkillsDesc3L1 = Lateral('- Strong Communication',mltply=x)
SkillsDesc3L2 = Lateral('- Team work',mltply=x)
SkillsDesc3L3 = Lateral('- Time Management',mltply=x)
SkillsDesc3L4 = Lateral('- Negotiation',mltply=x)
ExtrasTitle = Lateral('DataQuest\nData Scientist Path', mltply=x)

Languages = Lateral_title('Languages')
Language1 = Lateral('- English: c1')
Language2 = Lateral('- Spanish: b1')
Language3 = Lateral('- Polish: a2')

CodeTitle = Lateral_title('View Portfolio', mltply=x)

#defining the block trains

train_info = Train(Header1, Name1, Pers1)
train_title = Train(Title1)
train_projects = Train(ProjectsHeader, ProjectOneTitle, ProjectOneDescL1, ProjectTwoTitle, ProjectTwoDescL1, ProjectThreeTitle, ProjectThreeDesc)
train_work = Train(WorkHeader, WorkOneTitle, WorkOneTime, WorkOnePlace, WorkOneDescL1, WorkOneDescL2, WorkOneDescL3,
                            WorkTwoTitle, WorkTwoTime, WorkTwoPlace, WorkTwoDescL1, WorkTwoDescL2, WorkTwoDescL3,
                            WorkThreeTitle, WorkThreeTime, WorkThreePlace, WorkThreeDesc)
train_education = Train(EduHeader,EduOneTitle,EduOneTime,EduOnePlace,EduOneDesc1L1,EduOneDesc1L2,EduTwoTitle,EduTwoTime,EduOneDesc2L1,EduOneDesc2L2)

train_contact_title = Train(Info1)
train_contacts = Train(Contact1)

train_lateral_header = Train(SkillsHeader)

train_lateral_1 = Train(SkillsTitle1,
                     SkillsDesc1L1, SkillsDesc1L2, SkillsDesc1L3, SkillsDesc1L4, 
                     SkillsDesc1L5, SkillsDesc1L6, SkillsDesc1L7, SkillsDesc1L8,
                     SkillsDesc1L10)

train_lateral_2 = Train(SkillsTitle2,
                     SkillsDesc2L1, SkillsDesc2L2, SkillsDesc2L3, SkillsDesc2L4)
train_lateral_3 = Train(SkillsTitle3,
                     SkillsDesc3L1, SkillsDesc3L2, SkillsDesc3L3, SkillsDesc3L4)

train_language = Train(Languages, Language1, Language2, Language3)

train_code = Train(CodeTitle)

#setting plot
fig, ax = plt.subplots(figsize=(8.5*x, 11*x))

#in edit mode enable the following lines to show the ticks on upper x-axes
#ax2 = ax.twiny()

#remove axis
plt.axis('off')

#setting the colored bar (optional) in two parts
plt.axvline(x=.99, color=headers_color, alpha=1, linewidth=300*x)
plt.axhline(y=.8, xmin=0, xmax=1, color='#ffffff', linewidth=3)

#setting the paragraphs
personal_data = Paragraph((.2,.98), train_info)
title = Paragraph((.2, 0.855), train_title)

projects = Paragraph((.02, 0.82), train_projects)
work = Paragraph((0.02, 0.605),train_work)
edu = Paragraph((0.02, 0.2),train_education)

contact_title = Paragraph((0.76,0.980),train_contact_title)
contact = Paragraph((0.68,0.82),train_contacts)

skills_0 =Paragraph((0.76,0.775),train_lateral_header)
skills_1 = Paragraph((0.68,0.745),train_lateral_1)
skills_2 = Paragraph((0.68,0.525),train_lateral_2)
skills_3 = Paragraph((0.68,0.41),train_lateral_3)

language_ = Paragraph((0.68, 0.3), train_language)

code = Paragraph((0.68,0.205), train_code)

from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
arr_code = mpimg.imread(r'rcode.png')
imagebox = OffsetImage(arr_code, zoom=0.5)
ab = AnnotationBbox(imagebox, (0.84, 0.105))
ax.add_artist(ab)
my_pict = mpimg.imread(r'profile.jpg')
profilebox = OffsetImage(my_pict, zoom=0.5)
ab2 = AnnotationBbox(profilebox, (0.1, 0.925))
ax.add_artist(ab2)

plt.savefig(r'resumeexample.png', dpi=300, bbox_inches='tight')
plt.savefig(r'resumeexample.pdf', bbox_inches='tight')

plt.show()