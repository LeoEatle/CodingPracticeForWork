def getscore():
    n, r, avg = input().split(" ")
    n = int(n)
    r = int(r)
    avg = int(avg)
    course = []
    for i in range(int(n)):
        a, b = input().split(" ")
        course.append([int(a), int(b)])
    # sort the course list depends on the bi
    course.sort(key=lambda x: x[1])
    print (course)
    # caculate the score got
    score_now = 0
    course_num = len(course)
    for i in range(course_num):
        score_now = score_now + course[i][0]
    #print(score_now)
    score_need = int(avg) * course_num - score_now
    #print(score_need)

    # review the course as the sorted course until the score need
    score_review = 0
    time_review = 0
    for i in range(course_num):
        score_review = score_review + (r - course[i][0])
        time_review = time_review + course[i][1]*(r - course[i][0])
        print(time_review)
        if score_review > score_need:
            time_review = time_review - (score_review - score_need) * course[i][1]
            break
    return time_review

while (True):
    try:

        result =  getscore()
        print (result)
    except:
        break


