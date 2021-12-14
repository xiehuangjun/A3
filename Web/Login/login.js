const LoginForm =  document.getElementById("LoginForm");
LoginForm.addEventListener('submit', function (e) {             // Confirm whether the button click or not 
    e.preventDefault();

    let account = document.getElementById('account').value;
  
    //console.log(account);
    //console.log(identity);
    var formdata = new FormData(document.getElementById('LoginForm'));      // Creating a new formdata and listen the value of the form which named myForm in HTML
    fetch("http://IP:5000/login",{
            method: 'POST',
            body: formdata
        })
        .then(response => {return response.json()})
        .then(function(myJson){
            console.log(myJson);
            if(myJson.Log === "Login Success"){
                swal('Success', 'Login Successfully', 'success', {timer: 2000});
                var delayInMilliseconds = 1000;
                setTimeout(function() {
                    window.sessionStorage.setItem("User_account", account);
                    window.location.replace('../index.html');
                }, delayInMilliseconds);
            }else if(myJson.Log=="Login Failed"){
                swal('Fail', 'Login Fail', 'error')
            }
        }) 
        //   .then( (data) =>{render(data)})                 // Getting response then call function to do something
});

