document.addEventListener('submit',function(e){
  var f=e.target; if(!f.matches('[data-mailto]'))return; e.preventDefault();
  var v=function(n){var el=f.elements[n];return el?el.value:''};
  if(f.hasAttribute('data-broneering')){
    var p=f.elements['paev'];var paev=p&&p.length!==undefined?(f.querySelector('[name=paev]:checked')||{}).value:v('paev');
    var t=(f.querySelector('[name=teenus]:checked')||{}).value||'';var a=(f.querySelector('[name=aeg]:checked')||{}).value||'';
    var keha='Teenus: '+t+'\nPäev: '+paev+'\nKell: '+a+'\n\nNimi: '+v('nimi')+'\nTelefon: '+v('telefon');
    location.href='mailto:'+f.getAttribute('data-mailto')+'?subject='+encodeURIComponent('Broneering: '+t+', '+paev+' kell '+a)+'&body='+encodeURIComponent(keha);
    return;
  }
  var keha='Nimi: '+v('nimi')+'\nKontakt: '+v('kontakt')+'\nTöö: '+v('too')+'\n\n'+v('kirjeldus');
  location.href='mailto:'+f.getAttribute('data-mailto')+'?subject='+encodeURIComponent('Hinnapäring: '+v('too'))+'&body='+encodeURIComponent(keha);
});
document.addEventListener('DOMContentLoaded',function(){
  var P=['P','E','T','K','N','R','L'];
  document.querySelectorAll('[data-paevad]').forEach(function(box){
    var h='',d=new Date(),n=0;
    while(n<12){d.setDate(d.getDate()+1);if(d.getDay()===0)continue;
      var s=d.getDate()+'.'+(d.getMonth()+1)+'.';
      h+='<label class="kiip"><input type="radio" name="paev" value="'+P[d.getDay()]+' '+s+d.getFullYear()+'"'+(n?'':' required')+'><span>'+P[d.getDay()]+'<small>'+s+'</small></span></label>';n++;}
    box.innerHTML=h;
  });
});
