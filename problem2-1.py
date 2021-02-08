'''   Name: Michael Reece
      Ruid: 177000762
      problem2.py
      25/02/2019'''
''' This problem will open 3 files containing grades for the RUIDs
and will caluate the average of each homework, quiz, and exam.
it will then create a file and maake a chart of the grades.'''
import copy
# Import copy allows for a deep copy of the dict in the later function
def create_dictionary(idfilename, hwfilename, qzfilename, examfilename):
    # This will make the dictionary of the RUID with the amount of grades for each grade
    id_file = open(idfilename, 'r')
    sdata_dict = {}
    for idnum in id_file:
        idnum = idnum.rstrip()
        sdata_dict[idnum] = {'hw':listfunction(idnum, hwfilename,4), 'quiz':listfunction(idnum, qzfilename,8), 'exam':listfunction(idnum, examfilename,2) }
    id_file.close()
    return sdata_dict

def listfunction(idnum, listfilename, n):
    list_file = open(listfilename, 'r')
    grades = [int(line_1.split()[1]) for line_1 in list_file if line_1.split()[0] == idnum]
    while len(grades) < n:
        grades.append(0)
    list_file.close()
    return grades
    

def create_graderoster(sdata_dict, outfilename):
    # This function will format and make the table in the file
    outfile = open(outfilename, 'w')
    outfile.write('{:<14} {:>10} {:>10} {:>10} {:>12} {:>10}\n'.format('RUID','HW(30)','QUIZ(30)','EXAM(40)','TOTAL(100)','GRADE'))
    outfile.write('-' * 71)
    outfile.write('\n')
    sdata_Dict = sdata_dict.copy()
    id_avg = {'hw':[], 'quiz':[], 'exam':[],'score':[]}
    for key in sdata_Dict:          
        outfile.write('{:<14} {:>10.2f} {:>10.2f} {:>10.2f} {:>12.2f} {:>10} \n'.format(key, gradesCalculator(key,sdata_Dict,id_avg,1)[0], gradesCalculator(key,sdata_Dict,id_avg)[1], 
        gradesCalculator(key,sdata_Dict,id_avg)[2], gradesCalculator(key,sdata_Dict,id_avg)[3], gradesCalculator(key,sdata_Dict,id_avg)[4]))
    outfile.write('\n')
    outfile.write('{:>14} {:>10.2f} {:>10.2f} {:>10.2f} {:>12.2f} \n'.format('Maximum', max(id_avg['hw']), max(id_avg['quiz']), max(id_avg['exam']), max(id_avg['score'])))
    outfile.write('{:>14} {:>10.2f} {:>10.2f} {:>10.2f} {:>12.2f} \n'.format('Minimum', min(id_avg['hw']), min(id_avg['quiz']), min(id_avg['exam']), min(id_avg['score'])))
    outfile.write('{:>14} {:>10.2f} {:>10.2f} {:>10.2f} {:>12.2f} \n'.format('Average', sum(id_avg['hw'])/len(id_avg['hw']), sum(id_avg['quiz'])/len(id_avg['quiz']), sum(id_avg['exam'])/len(id_avg['exam']), sum(id_avg['score'])/len(id_avg['score'])))
    outfile.close()

def gradesCalculator(key, dictionary, student_dictionary, checker = 0):
    # This is where each RUID will run through the function and find the grade for each one
    dictionary = copy.deepcopy(dictionary)
    exam_average = ((sum(dictionary[key]['exam']))/2 * .2)
    dictionary[key]['hw'].remove(min(dictionary[key]['hw']))
    hw_average = (sum(dictionary[key]['hw'])/3)*.3
    dictionary[key]['quiz'].remove(max(dictionary[key]['quiz']))
    dictionary[key]['quiz'].remove(min(dictionary[key]['quiz']))
    quiz_average = (sum(dictionary[key]['quiz']) / 6) * .6
    total_score = hw_average + quiz_average + exam_average
    if checker == 1:
        student_dictionary['hw'].append(hw_average)
        student_dictionary['quiz'].append(quiz_average)
        student_dictionary['exam'].append(exam_average)
        student_dictionary['score'].append(total_score)
    if total_score >= 90:
        grade = 'A'
    elif total_score >= 85:
        grade = 'B+'
    elif total_score >= 80:
        grade = 'B'
    elif total_score >= 75:
        grade = 'C+'
    elif total_score >= 70:
        grade = 'C'
    elif total_score >= 60:
        grade = 'D'
    else:
        grade ='F'
    return hw_average, quiz_average, exam_average, total_score, grade
 
                  
if __name__ == "__main__":
    
    create_graderoster(create_dictionary('studentids.txt', 'hwscores.txt', 'quizscores.txt', 'examscores.txt'), 'graderoster.txt')  
