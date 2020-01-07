import copy
def create_dictionary(idfilename, hwfilename, qzfilename, examfilename):
    idfile = open(idfilename, 'r')
    sdata_dict = {}
    for idnumber in idfile:
        idnumber = idnumber.rstrip()
        sdata_dict[idnumber] = {'hw':hwfunction(idnumber, hwfilename), 'quiz':quizfunction(idnumber, qzfilename), 'exam':examfunction(idnumber, examfilename) }
    idfile.close()
    return sdata_dict

def hwfunction(idnumber, hwfilename):
    hwfile = open(hwfilename, 'r')
    hwGrades = [int(line1.split()[1]) for line1 in hwfile if line1.split()[0] == idnumber]
    while len(hwGrades) < 4:
        hwGrades.append(0)
    hwfile.close()
    return hwGrades

def quizfunction(idnumber, qzfilename):
    quizfile = open(qzfilename, 'r')
    quizGrades = [int(line2.split()[1]) for line2 in quizfile if line2.split()[0] == idnumber]
    while len(quizGrades) < 8:
        quizGrades.append(0)
    quizfile.close()
    return quizGrades

def examfunction(idnumber, examfilename):
    examfile = open(examfilename, 'r')
    examScores =[int(line3.split()[1]) for line3 in examfile if line3.split()[0] == idnumber]
    examfile.close()
    return examScores
    

def create_graderoster(sdata_dict, outfilename):
    outfile = open(outfilename, 'w')
    outfile.write('{:<14} {:>10} {:>10} {:>10} {:>12} {:>10}\n'.format('RUID','HW(30)','QUIZ(30)','EXAM(40)','TOTAL(100)','GRADE'))
    outfile.write('-' * 71)
    outfile.write('\n')
    sdata_Dict = sdata_dict.copy()
    for key in sdata_Dict:          
        outfile.write('{:<14} {:>10.2f} {:>10.2f} {:>10.2f} {:>12.2f} {:>10} \n'.format(key, gradesCalculator(key,sdata_Dict)[0], gradesCalculator(key,sdata_Dict)[1], 
        gradesCalculator(key,sdata_Dict)[2], gradesCalculator(key,sdata_Dict)[3], gradesCalculator(key,sdata_Dict)[4]))
    outfile.write('\n')
    outfile.write('{:>14} {:>10.2f} {:>10.2f} {:>10.2f} {:>12.2f} \n'.format('Maximum', max([gradesCalculator(key,sdata_Dict)[0] for key in sdata_Dict]),
                                                       max([gradesCalculator(key,sdata_Dict)[1] for key in sdata_Dict]), max([gradesCalculator(key,sdata_Dict)[2] for key in sdata_Dict]),
                                                       max([gradesCalculator(key,sdata_Dict)[3] for key in sdata_Dict])))
    outfile.write('{:>14} {:>10.2f} {:>10.2f} {:>10.2f} {:>12.2f} \n'.format('Minimum', min([gradesCalculator(key,sdata_Dict)[0] for key in sdata_Dict]),
                                                       min([gradesCalculator(key,sdata_Dict)[1] for key in sdata_Dict]), min([gradesCalculator(key,sdata_Dict)[2] for key in sdata_Dict]),
                                                       min([gradesCalculator(key,sdata_Dict)[3] for key in sdata_Dict])))
    outfile.write('{:>14} {:>10.2f} {:>10.2f} {:>10.2f} {:>12.2f} \n'.format('Average', sum([gradesCalculator(key,sdata_Dict)[0] for key in sdata_Dict])/len([gradesCalculator(key,sdata_Dict)[0] for key in sdata_Dict]),
                                                       sum(gradesCalculator(key,sdata_Dict)[1] for key in sdata_Dict)/len([gradesCalculator(key,sdata_Dict)[1] for key in sdata_Dict]),
                                                       sum(gradesCalculator(key,sdata_Dict)[2] for key in sdata_Dict)/len([gradesCalculator(key,sdata_Dict)[2] for key in sdata_Dict]),
                                                       sum(gradesCalculator(key,sdata_Dict)[3] for key in sdata_Dict)/len([gradesCalculator(key,sdata_Dict)[3] for key in sdata_Dict])))
    outfile.close()

def gradesCalculator(key, dictionary):
    Dictionary = copy.deepcopy(dictionary)
    examAverage = ((sum(Dictionary[key]['exam']))/2 * .2)
    Dictionary[key]['hw'].remove(min(Dictionary[key]['hw']))
    hwAverage = (sum(Dictionary[key]['hw'])/3)*.3
    Dictionary[key]['quiz'].remove(max(Dictionary[key]['quiz']))
    Dictionary[key]['quiz'].remove(min(Dictionary[key]['quiz']))
    quizAverage = (sum(Dictionary[key]['quiz']) / 6) * .6
    totalScore = hwAverage + quizAverage + examAverage
    if totalScore >= 90:
        grade = 'A'
    elif totalScore >= 85:
        grade = 'B+'
    elif totalScore >= 80:
        grade = 'B'
    elif totalScore >= 75:
        grade = 'C+'
    elif totalScore >= 70:
        grade = 'C'
    elif totalScore >= 60:
        grade = 'D'
    else:
        grade ='F'
    return hwAverage, quizAverage, examAverage, totalScore, grade

    

                  
if __name__ == "__main__":
    create_graderoster(create_dictionary('studentids.txt', 'hwscores.txt', 'quizscores.txt', 'examscores.txt'), 'gradeRoster.txt')  
