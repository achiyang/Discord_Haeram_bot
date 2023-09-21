from bs4 import BeautifulSoup

def make_list(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    courses = []

    course_elements = soup.find_all('li', class_=['course_label_re_01',['course_label_re_02']])
    for course_element in course_elements:
        course = {}
        course['course_title'] = course_element.find('h3').get_text()
        course['professor'] = course_element.find('p', class_='prof').get_text()
        course['course_link'] = course_element.find('a', class_='course_link')['href']
        course['image_src'] = course_element.find('img', class_='courseimage')['src']
        courses.append(course)

    return courses
