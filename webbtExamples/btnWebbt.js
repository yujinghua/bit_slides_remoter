BUTTON_SERVICE_UUID = 'e95d9882-251d-470a-a062-fa1922dfa9a8'
BUTTON_A_SERVICE_UUID = 'e95dda90-251d-470a-a062-fa1922dfa9a8'
BUTTON_B_SERVICE_UUID = 'e95dda91-251d-470a-a062-fa1922dfa9a8'

function btnA(event){
    var value = event.currentTarget.value.getInt8(0);
	console.log('A Value: ' + value);
    if(value == 0x01){
      Reveal.prev();    
    }
    
}

function btnB(event){
    var value = event.currentTarget.value.getInt8(0);
    console.log('B Value: ' + value);
    if(value == 0x01){
      Reveal.next();    
    }
}

function connect() {
	navigator.bluetooth.requestDevice({
        filters: [{
        	namePrefix: 'BBC micro:bit',
        }],
        optionalServices: [BUTTON_SERVICE_UUID] 
    })
        .then(device => {
            console.log('name = ', device.name);
            console.log('Got device:', device.name);
	        return device.gatt.connect();
        })
        .then(server => {
			return server.getPrimaryService(BUTTON_SERVICE_UUID);
        })
        .then(service => {
            btnService = service
            return btnService.getCharacteristic(BUTTON_A_SERVICE_UUID); //BUTTON1STATE_CHARACTERISTIC_UUID
        })
        .then(characteristicA => characteristicA.startNotifications())
        .then(characteristicA => {
        	characteristicA.addEventListener('characteristicvaluechanged', btnA);
        	return characteristicA.readValue();
        })

        .then(service => {
            return btnService.getCharacteristic(BUTTON_B_SERVICE_UUID); //BUTTON1STATE_CHARACTERISTIC_UUID
        })
        .then(characteristicB => characteristicB.startNotifications())
        .then(characteristicB => {
            characteristicB.addEventListener('characteristicvaluechanged', btnB);
            return characteristicB.readValue();
        })
        //.then(value => {
		  	//console.log('Serial number string: ' + value.getUint8(0)); 	
		//})
        .catch(error => { console.log(error); })
}

function disconnect() {
	
}