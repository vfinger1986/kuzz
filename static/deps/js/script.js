ymaps.ready(init)

function init(){
    let map = new ymaps.Map('mapp', {
        center: [57.839357566762814,28.310405999999997],
        zoom: 16
    });

    let placemark = new ymaps.Placemark([57.839357566762814,28.310405999999997], {balloonContent: '<strong>г. Псков, ул. Леона Поземского, д. 117. <br />+7 (953) 154 2613 <br /> +7 (921) 215 5603</strong>',
        iconCaption: 'Стальной Узор'}, {});
        

    map.controls.remove('geolocationControl'); 
    map.controls.remove('searchControl'); 
    map.controls.remove('trafficControl'); 
    map.controls.remove('typeSelector'); 
    map.controls.remove('fullscreenControl'); 
    map.controls.remove('zoomControl'); 
    map.controls.remove('rulerControl'); 

    map.geoObjects.add(placemark);


}