// ==UserScript==
// @name         Tarea 3 cryptografia
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Descifrar el mensaje secreto
// @author       Matogo
// @match        file://*/*
// ==/UserScript==

(function twofish(){
    'use strict';
    // Obtiene las variables
    var code = document.getElementsByClassName("twofish");
    var c = code[0].id;
    var key = document.getElementsByClassName("key");
    var k = key[0].id;
    // Descencripta el mensaje
    var decryted = twofish.decrypt(key,msg);
    // pop up con el mensaje descencriptado
    alert(str(decryted))
    
})();
