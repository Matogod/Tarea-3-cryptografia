// ==UserScript==
// @name         Tarea 3 cryptografia
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Descifrar el mensaje secreto
// @author       Matogo
// @match        file://*/*
// ==/UserScript==

(function() {
    'use strict';
    // Obtener el cifrado
    var code = document.getElementsByClassName("twofish");
    var c = code[0].id;
    // pop up con el cifrado
    alert(c);
})();