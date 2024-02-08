
function waterPlants(get) {

}
function redirectToServer(get) {
    console.log(this)
    window.location.href = "http://192.168.137.98:8080/output.html";
}
function togglerelay() {
    
    
    
    
    const command = 'python hello.py';
	exec(command, (error, stdout, stderr) => {});  
}
