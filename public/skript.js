document.addEventListener('submit',function(e){
  var f=e.target; if(!f.matches('[data-mailto]'))return; e.preventDefault();
  var v=function(n){var el=f.elements[n];return el?el.value:''};
  var keha='Nimi: '+v('nimi')+'\nKontakt: '+v('kontakt')+'\nTöö: '+v('too')+'\n\n'+v('kirjeldus');
  location.href='mailto:'+f.getAttribute('data-mailto')+'?subject='+encodeURIComponent('Hinnapäring: '+v('too'))+'&body='+encodeURIComponent(keha);
});
