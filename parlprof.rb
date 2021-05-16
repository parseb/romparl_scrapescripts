require 'nokogiri'
require 'open-uri'
require 'pry'
require 'pry-byebug'
require 'net/http'
require 'byebug'

prf='/pls/parlam/structura.mp?idm=3&leg=2016&cam=2'
t1=Net::HTTP.get('cdep.ro', prf)
  #t1= open(prfl)
doc= Nokogiri::HTML(t1)

z=doc.css('td .menuoff').text.split('.') || 'MISSING'
  name=z[0]
  yearb=z[-1].to_i
  #partyd= doc.css('td[bgcolor="#fffef2"] a')[1].text  || 'MISSING'
  partyd=t1[t1.index('</a></td><td>-</td><td>')+23..t1.index('</td></tr></table></td></tr>')-1]
  # doc.css('td td td td td td a').text  #doc.css('td a')[-10].text || 'MISSING'
  #county= doc.css('td[bgcolor="#fffef2"] a')[0].child.text || 'MISSING'
  c1= t1[t1.index('<td bgcolor="#fffef2" width="100%">')+82..t1.index('<td bgcolor="#fffef2" width="100%">')+150]
  county= c1[c1.index('">')+2..c1.index('</a>')-1]
  #legislat=t1[t1.index('legislatura 20')+12..t1.index('legislatura 20')+20 ]	
  
  legislat=doc.css('td[class="size1"] a b').text || 'MISSING'
  #typez= doc.css('td b')[3].text.to_s || 'MISSING'
  tipuri={'1'=>'Senator', '2'=>'Deputat'}
  typez=tipuri[prf[-1]] || 'Other'




puts name
puts yearb
puts partyd
puts county
puts legislat
puts typez


