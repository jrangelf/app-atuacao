function upperCase() {
  const x = document.getElementById("nomexeq");
  x.value = x.value.toUpperCase();
}


function inabValorAutor(situacao)
{	//alert("Situação da União " + situacao);

	if(situacao == "Autora")// valor do campo situação da união
        {
          //campos a serem habilitados
          document.getElementById("campo8").value = "";
          document.getElementById("campo8").readOnly=true;
        } else {
          document.getElementById("campo8").readOnly=false;	
        }
}


function inabcampo1()
{
  	//alert("selecionou campo2!");
  	document.getElementById("campo1").value = "";
}


function inabcampo2()
{
	//alert("selecionou campo1!");
	//alert(document.getElementById("campo2").value)		
	document.getElementById("campo2").value = "";
}


function valida1()
{	
	dt1=document.getElementById("dtenvio").value;
	dt2=document.getElementById("dtadvoga").value;

	if (dt1 > dt2)
	{
	    alert("A data do prazo do advogado não pode ser menor que a data de envio.");
	    document.getElementById("dtadvoga").value = "";
	    document.getElementById("dtenvio").focus();

	}
}


function valida2()
{
	
	dt1=document.getElementById("dtenvio").value;
	dt2=document.getElementById("dtsaida").value;


	if (dt1 > dt2)
	{
		alert("A data de saída não pode ser menor que a data de envio.");
	    document.getElementById("dtsaida").value = "";
	    document.getElementById("dtenvio").focus();
	}

}	


function noback()
{
	javascript:window.history.forward(1);	
}					


function atualizaRelogio() {
    var momentoAtual = new Date();
    var vhora = momentoAtual.getHours();
    var vminuto = momentoAtual.getMinutes();
    var vsegundo = momentoAtual.getSeconds();

	now = new Date;
    dayName = new Array("Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado")
    monName = new Array("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")
    var data = dayName[now.getDay()] + ", " + now.getDate() + " de " + monName[now.getMonth()] + " de " + now.getFullYear();
    document.getElementById("localdata").innerHTML = data;


    if (vhora < 10) {
        vhora = "0" + vhora;
    }
    if (vminuto < 10) {
        vminuto = "0" + vminuto;
    }
    if (vsegundo < 10) {
        vsegundo = "0" + vsegundo;
    }
    horaFormat = "  [" + vhora + ":" + vminuto + ":" + vsegundo + "]";
    document.getElementById("hora").innerHTML = horaFormat;
    setTimeout("atualizaRelogio()", 1000);
}


function doDecimal(pStr,campo)
{
											   
	var reDecimal = /^[+-]?((\d+|\d{1,3}(\.\d{3})+)(\,\d*)?|\,\d+)$/;
	charDec = ",";

	valorUniao = document.getElementById("campo9").value;
	valorAutor = document.getElementById("campo8").value;
					
	if (reDecimal.test(pStr)) {
		pos = pStr.indexOf(charDec);
		decs = pos == -1? 0: pStr.length - pos - 1;

	} else if (pStr != null && pStr != "") {
				alert("Valor " + pStr + " é inválido! Números apenas com decimais ou com decimais e separador de milhar são permitidos.");
				document.getElementById(campo).value = "";
	}

//	if  (campo == "campo8")
//	{
//		if (valorUniao > valorAutor)
//		{
//		alert("O valor da União não pode ser superior ao valor do Autor");
//		document.getElementById("campo9").value = document.getElementById("campo8").value;
//		} 
//	} 

	//if  (campo == "campo9" && valorAutor != "")
	//{
	//	if (valorUniao > valorAutor)
	//	{
	//	alert("O valor da União não pode ser superior ao valor do Autor");
	//	document.getElementById("campo9").value = document.getElementById("campo8").value;
	//	} 
	//} 


								    
} // doDecimal



function validaQtdExeq(valor){
					
	//alert ("quantidade de exequentes: "); // + numero);
	if (valor == 0) {
		alert("O número de exequentes não pode ser zero!");
		document.getElementById("cmp1").value = "";
	
	}
	if (valor < 0) {
		alert("O número de exequentes deve ser um valor positivo");
		document.getElementById("cmp1").value = "";
	
	}
	
	
								    
}