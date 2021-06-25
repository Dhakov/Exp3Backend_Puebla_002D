function validacion()
{
    user = document.getElementById('user').value;
    pass = document.getElementById('pass_user').value;
    pass_re = document.getElementById('pass_user_re').value;

    if (pass != pass_re)
    {
        alert('Error, las contraseñas no coinciden');
        document.getElementById('pass_user_re').value = "";
        document.datos.pass.focus();
        return false;
    }

    if(user == null || user.length==0 || /^\s+$/.test(user))
    {
        alert('Error, ingrese un nombre de usuario valido');
        document.getElementById('user').value="";
        document.datos.user.focus();
        return false;
    }
}


function textMinus(argumento)
{
    argumento.value = argumento.value.toLowerCase();
}        

function checkSesion(argumento)
{

    checkbox = document.getElementById('check_sesion')

    if (checkbox.checked)
    {
        document.getElementById('check_user').disabled = false;
        document.getElementById('check_correo').disabled = false;
        document.getElementById('check_user').checked = false;
        document.getElementById('check_correo').checked = false;
    }
    else
    {
        document.getElementById('check_user').disabled = true;
        document.getElementById('check_correo').disabled = true;
        document.getElementById('check_user').checked = true;
        document.getElementById('check_correo').checked = true;
    }
    
}
