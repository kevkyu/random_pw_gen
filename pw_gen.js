const passwordBox = document.getElementById("password")
const length = 16;

const digits = "0123456789"
const lower = "abcdefghijklmnopqrstuvwxyz"
const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
const symbols = "!#$%&()*+,-./"

const all = digits + lower + upper + symbols;

function createPassword(){
    let password = "";
    password += digits[Math.floor(Math.random() * digits.length)];
    password += lower[Math.floor(Math.random() * lower.length)];
    password += upper[Math.floor(Math.random() * upper.length)];
    password += symbols[Math.floor(Math.random() * symbols.length)];

    while (length > password.length){
        password += all[Math.floor(Math.random() * all.length)];
    }
    passwordBox.value = password;
}

function copyPassword(){
    passwordBox.select();
    document.execCommand("copy");
}