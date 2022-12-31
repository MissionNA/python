# quiz)사이트별 비번 만드는 프로그램을 작성하시오

#예 http://naver.com
#규칙1:http:// 부분을 제외 =>naver.com
#규칙2:첨만나는점(.) 이후 부분은 제외 =>naver
#규칙3:남은 글자 중 처음 세자리 + 글자 갯수 +글자내 'e' 갯수 + '!'로 구성
#                          (nav)     (5)              (1)       (!)
#예)생성된 비밀번호:nav51!

url = 'http://naver.com'
my_str=url.replace('http://','')
# print(my_str)
# my_str =my_str[:3]
# print(my_str)
my_str=my_str[:my_str.index(".")]
# print(my_str)

pw =my_str[:3] + str(len(my_str)) + str(my_str.count('e')) +'!' #첫 str은 정수를 str로 바꿈
print(pw)
