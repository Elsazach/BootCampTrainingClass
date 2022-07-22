package main
import "fmt"
func fib(num int){
    var n1 int=0
    var n2 int=1
    var n3 int=0
    
   for i := 1; i <= num; i++ {
     fmt.Print(n1," ")
     n3 = n1 + n2
     n1 = n2
     n2 = n3
 
}
}
func main(){
    
    fib(5)
    
    
