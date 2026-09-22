(function(){
  var page=document.querySelector('.wall'),state='',own=false;
  function read(){var m=location.hash.match(/sector=([^&]*)/);state=m?decodeURIComponent(m[1]):'';}
  function write(){var h=state?'#sector='+encodeURIComponent(state):'';if(h!==location.hash){own=true;if(h)location.hash=h;else history.replaceState(null,'',location.pathname);setTimeout(function(){own=false;},0);}}
  function apply(){
    document.querySelectorAll('.sectors a').forEach(function(x){x.toggleAttribute('aria-current',x.getAttribute('data-val')===state);});
    var n=0;document.querySelectorAll('.tile').forEach(function(t){var ok=!state||t.getAttribute('data-sector')===state;t.hidden=!ok;if(ok)n++;});
    var e=document.querySelector('.wall .empty');if(e)e.hidden=n>0;
  }
  page.addEventListener('click',function(e){var a=e.target.closest('.sectors a');if(!a)return;e.preventDefault();var v=a.getAttribute('data-val');state=(state===v)?'':v;write();apply();});
  window.addEventListener('hashchange',function(){if(own)return;read();apply();});
  read();apply();
})();
