#python을 이용한 quicksort
import sys

def quick_sort(arr,left,right,key):
            if left >= right:
                return
            pivot = arr[right-1] # 리스트 시작이 0이라서
            i=left
            j=right-2
            while i <= j:
                while(key(arr[i],pivot)):#lambda 이용
                    i+=1
                while(not arr[j] == pivot and not key(arr[j],pivot)):#lambda 이용 소름;
                    j-=1
                if(i<=j):
                    swap(arr,i,j)
                    i+=1; j-=1
            swap(arr,i,right-1)#한번 다 끝나면 pivot 중간으로 옮기기
            quick_sort(arr, left, i ,key)#pivot보다 작은수 재귀
            quick_sort(arr, i+1, right, key)#pivot보다 큰수 재귀
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

if __name__=="__main__":
    argv = sys.argv

if(len(argv)<5) or not ("-o" in argv and "-i" in argv): # 리스트부분이 1이거나 argv에 -o,-i가없으면
    print("Wrong argvs : {}".format(argv)) # 잘못됬다 표시하고 배열 기초
    sys.exit()

arr = list(map(int,argv[4:]))#[int(x) for x in argv[4:]]로 대체가능!

if argv[(argv.index("-o"))+1] == "A":
    quick_sort(arr,0,len(arr),lambda x,y : x < y)
elif argv[(argv.index("-o"))+1] == "D":
    quick_sort(arr,0,len(arr),lambda x,y : x > y)#elif 오류 계속남 들여쓰기 제대로할것

print(arr)
