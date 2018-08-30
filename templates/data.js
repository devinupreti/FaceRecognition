/**
 * Created by DEVIN UPRETI on 4/5/2017.
 */

function readFile(){
    JQuery.get('data.txt', function(txt){
       $('#output').text(txt);
       document
    });
 }



//document.getElementById("openFile").addEventListener('change', function() {
//    var fr = new FileReader();
//    fr.onload = function() {
//        document.getElementById("fileContents").textContent = this.result;
//    }
//    fr.readAsText(this.files[0]);
// })
//

//<input type ="file" id = "openFile" />
//            <br>
//            <pre id="fileContents" ></pre>

