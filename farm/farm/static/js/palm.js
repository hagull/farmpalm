function abc() {
  if( window.screen.width > 768){
    m_btn(value='on');
  }
  else {
    m_btn(value='off');
  }
}


function m_btn(){
  var c_nav = document.getElementsByClassName('control-nav');
  var value = "off";
  if( this.value == 'off') {
    this.value = 'on';
    c_nav[0].style.display = 'none';
  } else {
    this.value='off';
    c_nav[0].style.display = 'block';
  }
}
