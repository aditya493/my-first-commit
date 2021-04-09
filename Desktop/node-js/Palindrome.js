
    
function isPlaindrome(S){
          const len =S.length;
    for (let i = 0; i < len / 2; i++) {        

        if (S[i] == S[len - 1 - i]) {

            return true;
        }

    }
    return false;

}
       


console.log(isPlaindrome("aabb"));