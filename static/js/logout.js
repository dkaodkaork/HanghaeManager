function logout() {
    $.removeCookie('mytoken', {path:'/'});
    alert('로그아웃!')
    window.location.href = '/login'
}
//  로그아웃 버튼 만들어서 붙이시면 됩니다