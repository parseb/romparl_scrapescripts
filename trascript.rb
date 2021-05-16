

#require 'open-uri'
require 'net/http'


#8214 - 27.10.20
#2004
c=2004
8214.times do
    cz=c.to_s
    lnk= '/pls/steno/steno.stenograma?ids='+cz
    t1= Net::HTTP.get('cdep.ro', lnk)
    doc= Nokogiri::HTML(t1)
    p '====='+cz+'====='
    dateraw=doc.css('.headline').children.text.split(" ").map(&:strip)
    yearz= dateraw.last 
    #@item.property = if params[:property] == nil then true else false end
    monthz=dateraw[-2]
    dayz=dateraw[-3] 
    texts= doc.css('.textn')
    
    texts.each do |t|
    headline= doc.css('span[class="headline"]').text
        name= t.children.css('a').text.length>5 ? t.children.css('a').text : 'OTHER'
        
        if !t.children.children.css('a')[0].nil?
            profile_link= 'http://www.cdep.ro' + t.children.children.css('a')[0].attributes['href'].value || 'MISSING'
            if profile_link.include?('&') && profile_link != 'MISSING'
                z= profile_link.split('&')
                #byebug
                z= z[0]+'&'+z[-1]+'&'+z[1]
                profile_link= z[18..-1]
                #byebug
            end
            end
        #text= t.text.search('//text()').map(&:text).delete_if{|x| x !~ /\w/}
        text=t.text.length > 20 ? t.text : 'smaller than 50 chars'
        if text != 'smaller than 50 chars'
            #binding.pry	
            puts profile_link
            #puts name
            puts text
            #puts monthz
            #puts dayz
            puts yearz
            p '==============='
            thisspeech = Speech.new()
            thisspeech.speaker_name= name
            thisspeech.year= yearz 
            thisspeech.month= monthz
            thisspeech.day= dayz
            thisspeech.content= text
            thisspeech.title= headline
            thisspeech.profile_url= profile_link
            #byebug
            if profile_link
                thisspeech.mp_id=Mp.where(profile_url: profile_link).ids
            else
                thisspeech.mp_id= Mp.find(2989).id
            end
            thisspeech.save!
            end
        end

    c=c+1
    sleep(10)
    end
    