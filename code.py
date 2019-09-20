from bs4 import BeautifulSoup
html_doc = """<!DOCTYPE html>
    <html lang="es-ES" prefix="og:http://ogp.me/ns#">
    <head>
    <title>Universidad Francisco Marroquín</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="title" content="Universidad Francisco Marroquín"/>
    <meta name="description" content="Nuestra misión es la enseñanza y difusión de los principios éticos, jurídicos y económicos de una sociedad de personas libres y responsables.
    "/>
    <meta name="keywords" content="Educación, Educación Superior, Verdad, Libertad, Justicia, Universidad, Universidad Francisco Marroquín, Francisco Marroquín, UFM, Coraje, Fortaleza, Sabiduría, Nobleza, Arquitectura, Ciencias Económicas, Ciencias Sociales, Derecho, Educación, Estudios Políticos y Relaciones Internacionales, Medicina, Nutrición, Odontología, Psicología, Acton MBA, Escuela de Cine y Artes Visuales, Escuela de Negocios, Escuela de Posgrado, Michael Polanyi College"/>
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="Universidad Francisco Marroquín"/>
    <meta property="og:url" content="https://www.ufm.edu"/>
    <meta property="og:image" content="http://www.ufm.edu/logo_institucional/LogoUFM200x200.png"/>
    <meta property="og:image:secure_url" content="https://www.ufm.edu/logo_institucional/LogoUFM200x200.png"/>
    <meta property="og:description" content="Nuestra misión es la enseñanza y difusión de los principios éticos, jurídicos y económicos de una sociedad de personas libres y responsables.
    "/>
    <meta name="msvalidate.01" content="2D8BF85B6AEA4FC42A2CCF9D18A2B56A"/>

    <meta name="norton-safeweb-site-verification" content="u51duo9or17ntoxqmztukbcrz4ci1co9ej1tl2nh9c4lt4u0gumcxm3vs2ckmd9h6zzuqn1cjdio5xug69zlv9ptfp8nddj6c1460gw39yn5vhd4fw6944kgour5eof4"/>

    <meta name="keywords" content="keyword1, keyword2,nsw-u51duo9or17ntoxqmztukbcrz4ci1co9ej1tl2nh9c4lt4u0gumcxm3vs2ckmd9h6zzuqn1cjdio5xug69zlv9ptfp8nddj6c1460gw39yn5vhd4fw6944kgour5eof4"/>


    <link rel="shortcut icon" href="/favicon.ico"/>
    <link href="/skins/Ufm/A.plugins,,_bootstrap-2.3.2,,_css,,_bootstrap.min.css+css,,_bootstrap-responsive.css+plugins,,_font-awesome-4.1.0,,_css,,_font-awesome.min.css,Mcc.KOfmUBfgiP.css.pagespeed.cf.ZRl_P9VyQF.css" rel="stylesheet"/>


    <!--[if IE 7]><link rel="stylesheet" href="/skins/Ufm/plugins/font-awesome-4.1.0/css/font-awesome-ie7.min.css"><![endif]-->
    <link href="/skins/Ufm/css/A.skin.css.pagespeed.cf.RiDDD0FrLy.css" rel="stylesheet">
    <!--[if gte IE 9]><link href="/skins/Ufm/css/skin-ie9.css" rel="stylesheet"><![endif]-->

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="/skins/Ufm/plugins,_bootstrap-2.3.2,_js,_bootstrap.min.js+js,_jquery.jcarousel.min.js+js,_skin.js.pagespeed.jc.ROb9CFkRks.js"></script><script>eval(mod_pagespeed_0ra11xnNjP);</script>
    <script>eval(mod_pagespeed_J6MAwphJqx);</script>
    <script>eval(mod_pagespeed_oqI0Td9oGZ);</script>
    <!--[if lt IE 9]><script src="/skins/Ufm/js/html5shiv.js"></script><![endif]-->

    <style type="text/css">#push{height:10px}.social .fa{font-size:30px;color:#bab6b6;text-decoration:none}.social .fa:hover{color:#ccc}.menu-value{height:407px;opacity:.92;filter: alpha(opacity=92);background:#303030;border-bottom:#606060 5px solid}#mycarousel a{color:#fff}#cargandox{position:absolute;top:0;left:0;width:160px}#topmenu a{color:#696969}#topmenu{position:relative;float:right}#topmenu ul{margin:0;padding:0;padding-right:10px}#topmenu li{display:inline;position:relative;float:left;padding:0 8px;border-left:1px dotted #999}#topmenu li:first-child{padding-left:0;border-left:none}#topmenu li:last-child{padding-right:0}.nodesplegar{display:none}.titulo.active{font-weight:bold}.titulo:last{border-color:#fff}.jcarousel-skin-ie7 .jcarousel-container{font-size:85%}.jcarousel-skin-ie7 .jcarousel-container-horizontal{width:250px;padding:0 0 0 0}.jcarousel-skin-ie7 .jcarousel-clip{overflow:hidden}.jcarousel-skin-ie7 .jcarousel-clip-horizontal{width:250px;height:390px}.jcarousel-skin-ie7 .jcarousel-item{width:250px;height:400px;color:#fff!important;padding-top:12px}.jcarousel-skin-ie7 .jcarousel-item:hover,.jcarousel-skin-ie7 .jcarousel-item:focus{border-color:gray}.jcarousel-skin-ie7 .jcarousel-item-horizontal{margin-left:0;margin-right:7px}.jcarousel-skin-ie7 .jcarousel-direction-rtl .jcarousel-item-horizontal{margin-left:7px;margin-right:0}.jcarousel-skin-ie7 .jcarousel-next-horizontal{position:absolute;bottom:-10px;right:8px;width:20px;height:20px;cursor:pointer;background:transparent url(/skins/Ufm/img/xspriteOpt_2.png.pagespeed.ic.1z71rUATz4.webp) no-repeat;background-position:-2px -4px}.jcarousel-skin-ie7 .jcarousel-next-horizontal:hover,.jcarousel-skin-ie7 .jcarousel-next-horizontal:focus{background-position:-2px -24px}.jcarousel-skin-ie7 .jcarousel-next-disabled-horizontal,.jcarousel-skin-ie7 .jcarousel-next-disabled-horizontal:hover,.jcarousel-skin-ie7 .jcarousel-next-disabled-horizontal:focus,.jcarousel-skin-ie7 .jcarousel-next-disabled-horizontal:active{cursor:default;background-position:0 100px}.jcarousel-skin-ie7 .jcarousel-prev-horizontal{position:absolute;bottom:-10px;left:5px;width:20px;height:20px;cursor:pointer;background:transparent url(/skins/Ufm/img/xspriteOpt_2.png.pagespeed.ic.1z71rUATz4.webp) no-repeat;background-position:-2px -64px}.jcarousel-skin-ie7 .jcarousel-prev-horizontal:hover,.jcarousel-skin-ie7 .jcarousel-prev-horizontal:focus{background-position:-2px -84px}.jcarousel-skin-ie7 .jcarousel-prev-disabled-horizontal,.jcarousel-skin-ie7 .jcarousel-prev-disabled-horizontal:hover,.jcarousel-skin-ie7 .jcarousel-prev-disabled-horizontal:focus,.jcarousel-skin-ie7 .jcarousel-prev-disabled-horizontal:active{cursor:default;background-position:0 100px}.imagen a img{-webkit-filter:grayscale(.9);filter:grayscale(.9);-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";filter: alpha(opacity=50)}.menu-padding{padding-top:5px}#actual{cursor:pointer;position:absolute;width:185px;margin-left:30px;text-align:center;color:#ccc;font-size:14px;margin-top:-10px;z-index:10}@media (min-width:980px){.fondo_cita_posicion{position:absolute;left:0;top:0}.menu-value{font-size:.95em}.menu-value ul li{padding:2px 0}}@media (max-width:979px){#actual{cursor:pointer;position:absolute;width:185px;margin-left:30px;text-align:center;color:#ccc;font-size:14px;margin-top:-10px;z-index:10}.fondo_cita_posicion{position:absolute;left:0;top:0}.menu-padding{padding-top:0}.menu-value{font-size:.7em}.menu-value div ul li a{margin:0!important;padding:0!important}}</style>

            <!-- Begin facebook Embed Code -->
            <!-- <script>
                    (function() {
                    var _fbq = window._fbq || (window._fbq = []);
                    if (!_fbq.loaded) {
                        var fbds = document.createElement('script');
                        fbds.async = true;
                        fbds.src = '//connect.facebook.net/en_US/fbds.js';
                        var s = document.getElementsByTagName('script')[0];
                        s.parentNode.insertBefore(fbds, s);
                        _fbq.loaded = true;
                    }
                    _fbq.push(['addPixelId', '776336172407563']);
                    })();
                    window._fbq = window._fbq || [];
                    window._fbq.push(['track', 'PixelInitialized', {}]);
                    </script> -->
            <!-- <noscript>
            <img height="1" width="1" alt="" style="display:none" src="https://www.facebook.com/tr?id=776336172407563&amp;ev=PixelInitialized" />
            </noscript> -->
            <!-- Begin fabebook Embed Code -->

            <!-- Begin Inspectlet Embed Code -->
            <script type="text/javascript" id="inspectletjs">window.__insp=window.__insp||[];__insp.push(['wid',900962822]);(function(){function __ldinsp(){var insp=document.createElement('script');insp.type='text/javascript';insp.async=true;insp.id="inspsync";insp.src=('https:'==document.location.protocol?'https':'http')+'://cdn.inspectlet.com/inspectlet.js';var x=document.getElementsByTagName('script')[0];x.parentNode.insertBefore(insp,x);}if(window.attachEvent){window.attachEvent('onload',__ldinsp);}else{window.addEventListener('load',__ldinsp,false);}})();</script>
            <!-- End Inspectlet Embed Code -->

            <!-- Google Javascript -->
            <!-- <script>
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
            })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

            ga('create', 'UA-404175-1', 'auto');
            ga('send', 'pageview');
            </script> -->
            <!-- Google Javascript -->

            <!-- Start Alexa Certify Javascript -->
                <script type="text/javascript">_atrk_opts={atrk_acct:"Lb4Mn1QolK10uG",domain:"ufm.edu",dynamic:true};(function(){var as=document.createElement('script');as.type='text/javascript';as.async=true;as.src="https://d31qbv1cthcecs.cloudfront.net/atrk.js";var s=document.getElementsByTagName('script')[0];s.parentNode.insertBefore(as,s);})();</script>
                <noscript><img src="https://d5nxst8fruw4z.cloudfront.net/atrk.gif?account=Lb4Mn1QolK10uG" style="display:none" height="1" width="1" alt=""/></noscript>
            <!-- End Alexa Certify Javascript -->

            <!-- Start eloqua -->
            <!-- <script type="text/javascript">
                var _elqQ = _elqQ || [];
                _elqQ.push(['elqSetSiteId', '1232663870']);
                _elqQ.push(['elqTrackPageView']);

                (function () {
                    function async_load() {
                        var s = document.createElement('script'); s.type = 'text/javascript'; s.async = true;
                        s.src = '//img04.en25.com/i/elqCfg.min.js';
                        var x = document.getElementsByTagName('script')[0]; x.parentNode.insertBefore(s, x);
                    }
                    if (window.addEventListener) window.addEventListener('DOMContentLoaded', async_load, false);
                    else if (window.attachEvent) window.attachEvent('onload', async_load);
                })();
            </script> -->
            <!-- End eloqua -->
            <!-- Google Tag Manager -->
            <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-NKHPQFD');</script>
            <!-- End Google Tag Manager -->		
            <!-- Pardot -->
            <script type="text/javascript">piAId='706513';piCId='1530';piHostname='pi.pardot.com';(function(){function async_load(){var s=document.createElement('script');s.type='text/javascript';s.src=('https:'==document.location.protocol?'https://pi':'http://cdn')+'.pardot.com/pd.js';var c=document.getElementsByTagName('script')[0];c.parentNode.insertBefore(s,c);}if(window.attachEvent){window.attachEvent('onload',async_load);}else{window.addEventListener('load',async_load,false);}})();</script>
            <!-- End Pardot -->
    </head>
    <body>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NKHPQFD" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->	
    <!--
    <div style="padding:10px 0 10px 0; margin-bottom:5px; text-align:center; border-bottom:2px solid silver; background:#cfcfcf;"> VERSION BETA </div>
    172.25.1.85--190.104.124.28--https-->
    <!-- mobil -->
    <div id="frame">
    <div id="sidebar">
    <div style="padding:5px 15px;">
        <form class="navbar-form" style="margin:0;" id="searchform" method="GET" action="/Especial:Busqueda">
        <div class="input-append" style="margin:0;">
            <input name="q" class="input-small" type="text" style="-webkit-border-radius:0;-moz-border-radius:0;border-radius:0; margin:0; ">
            <button id="button_searchform" class="btn" type="button" style="-webkit-border-radius:0;-moz-border-radius:0;border-radius:0; "><i class="icon-search"></i></button>
        </div>
        </form>
    </div>

    <!-- sidebar -->
    <div style="padding:5px 15px;"> <div class="span2">
    <div class="dsuperior">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/english/">UFM Key Projects</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://foufm.org">Friends of UFM</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/checkout/donaciones/">Donaciones</a></li>
    <li><a href="/Especial:Sugerencias" title="Especial:Sugerencias"> Contáctenos</a></li></ul>
    </div>
    </div>
    <div class="span2">
    <div class="dsuperior">
    <ul><li><b><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://admisiones.ufm.edu/">Admisiones</a></b></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://alumni.ufm.edu/">Alumni</a></li>
    <li><b><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://madrid.ufm.edu/?referer=ufm">Campus Madrid</a></b></li>
    <li><a href="/Redes_Sociales" title="Redes Sociales"> Redes Sociales</a></li></ul>
    </div>
    </div>
    <br/>
    </div>
    
                            <div style="padding:0 15px;"><a href="/index.php/Estudios">Estudios</a></div>
                            <hr/><div class="accordion" id="accordion2">  
        <div class="accordion-group">
            <div class="accordion-heading">
            <a class="accordion-toggle menucerrado" data-toggle="collapse" data-parent="#accordion2" href="#facultades">
                Facultades <i class="fa fa-arrow-down"></i>
            </a>
            </div>
            <div id="facultades" class="accordion-body collapse in">
            <div class="accordion-inner">
                <div class="row-fluid">
    <div class="span4 hidden-phone"><div class="row-fluid"><div class="span12" style="margin-top:10px; text-align:center; color:#808080;"><img src="/skins/Ufm/img/xnobleza3.png.pagespeed.ic.Dxml1DdkI_.webp" width="60%" style="margin-bottom:5px;"/><br/>La continua prueba de confianza que debemos dar a los demás en nuestra convivencia diaria.</div></div></div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://arquitectura.ufm.edu">Arquitectura</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://chh.ufm.edu">Centro Henry Hazlitt</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://fce.ufm.edu">Ciencias Económicas</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://escs.ufm.edu">Ciencias Sociales</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://derecho.ufm.edu">Derecho</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://educacion.ufm.edu">Educación</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://epri.ufm.edu">Estudios Políticos y Relaciones Internacionales</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://medicina.ufm.edu">Medicina</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://nutricion.ufm.edu">Nutrición</a></li></ul>
    </div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://odontologia.ufm.edu">Odontología</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://psicologia.ufm.edu">Psicología</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://actonmba.ufm.edu">Acton MBA</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://doctorado.ufm.edu">Programa de Doctorado</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://cine.ufm.edu/">Escuela de Cine y Artes Visuales</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://en.ufm.edu/">Escuela de Negocios</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://posgrado.ufm.edu/">Escuela de Posgrado</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://mpc.ufm.edu/">Michael Polanyi College</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://madrid.ufm.edu/">Campus Madrid</a></li></ul>
    </div>
    </div>

            </div>
            </div>
        </div>
        
        <div class="accordion-group">
            <div class="accordion-heading">
            <a class="accordion-toggle menucerrado" data-toggle="collapse" data-parent="#accordion2" href="#proyectos">
                Proyectos <i class="fa fa-arrow-down"></i>
            </a>
            </div>
            <div id="proyectos" class="accordion-body collapse in">
            <div class="accordion-inner">
                <div class="row-fluid">
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://antiguaforum.ufm.edu">Antigua Forum</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://arboretum.ufm.edu/">Arboretum</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://debates.ufm.edu/">Asociación de Debates</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://chh.ufm.edu">Centro Henry Hazlitt</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://doshistorias.ufm.edu/">Dos Historias, Una Ciudad</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://cadep.ufm.edu">Centro para el Análisis de las Deciones Públicas (CADEP)</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://hume.ufm.edu">Centro de Ética David Hume</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://capitalismo.ufm.edu/">Centro de Estudio del Capitalismo</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://centroik.ufm.edu">Centro Ibn Khaldun</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://fce.ufm.edu/inicio-cvs/">Centro Vernon Smith de Economía Experimental</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://cff.ufm.edu/2019/">College Freedom Forum At UFM 2019</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.stillman.ufm.edu/">Concurso Charles L. Stillman </a></li></ul>
    </div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://economia-austriaca.ufm.edu/">Congreso de Economía Austriaca</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://evolucion.ufm.edu/">Evolución</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://frc.ufm.edu/">Finance Research Center</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://gem.ufm.edu/">Global Entrepreneurship Monitor</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://grajedamena.ufm.edu/">Grajeda Mena</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.freedomsphilosopher.ufm.edu/index.php/Main_Page">Hayek Freedom's Philosopher</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://hazlitt.ufm.edu">Henry Hazlitt Archives</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://heuristica.ufm.edu">Heurística</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://jihu.ufm.edu">Jornadas de Investigación en Humanidades (JIHU)</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://fce.ufm.edu/kec/centro-de-emprendimiento-kirzner/">Kirzner Entrepreneurship Center</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://trends.ufm.edu/">Market Trends Es/En</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://donquijote.ufm.edu/">Mooc Don Quijote Es/En</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://salamanca.ufm.edu">Mooc La Escuela de Salamanca Es/En</a></li></ul>
    <p><br/>
    </p>
    </div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://opencourses.ufm.edu/courses/course-v1:Ciencia-Politica+CSESV1+2019/about">Mooc Capitalismo y Socialismo</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://opencourses.ufm.edu/courses/course-v1:Estudios-latinoamericanos+DMLES+2019/about">Mooc Dictaduras Militares Latinoamericanas</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://opencourses.ufm.edu">Open Courses</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.plazalibertad.ufm.edu">Plaza de la Libertad</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://pozoeconomico.ufm.edu">Pozo Económico</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://ita.ufm.edu">Programa ITA</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://grandeslibros.ufm.edu/">Seminario de Grandes Libros</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://semilladelibertad.ufm.edu/">Semilla de Libertad</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://escolasticos.ufm.edu">Sitio Escolástico</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://tedx.ufm.edu">TEDxUFM</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://hayek.ufm.edu">The Hayek Interviews</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://journal.apee.org">The Journal of Private Enterprise</a></li></ul>
    </div>
    </div>

            </div>
            </div>
        </div>
        
        <div class="accordion-group">
            <div class="accordion-heading">
            <a class="accordion-toggle menucerrado" data-toggle="collapse" data-parent="#accordion2" href="#recursos">
                Recursos <i class="fa fa-arrow-down"></i>
            </a>
            </div>
            <div id="recursos" class="accordion-body collapse in">
            <div class="accordion-inner">
                <div class="row-fluid">
    <div class="span4 hidden-phone"><div class="row-fluid"><div class="span12" style="margin-top:10px; text-align:center; color:#808080;"><img src="/skins/Ufm/img/xcoraje3.png.pagespeed.ic.B5aLhnNuSK.webp" width="70%" style="margin-bottom:5px;"/><br/>La decisión y el valor de nuestras iniciativas.</div></div></div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://alumni.ufm.edu/">Alumni</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://akademeia.ufm.edu/index.php/P%C3%A1gina_principal">Akademeia</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://arboretum.ufm.edu">Arboretum</a></li>
    <li><a href="/Asociaciones_Estudiantiles" title="Asociaciones Estudiantiles"> Asociación de Estudiantes</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://biblioteca.ufm.edu">Biblioteca</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://bookstore.ufm.edu">Bookstore</a></li>
    <li><a href="/Calendario_Acad%C3%A9mico_2019" title="Calendario Académico 2019">Calendario Académico 2019</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.ceta.ufm.edu">CETA</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://gt.creativecommons.org">Creative Commons</a></li>
    <li><a href="/Cr%C3%A9dito_Educativo" title="Crédito Educativo">Crédito Educativo</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://cronica.ufm.edu/">Crónica</a></li></ul>
    <p><br/>
    </p>
    </div>
    <div class="span4">
    <ul><li><a href="/Directorio" title="Directorio">Directorio</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://asomate.ufm.edu/">Eventos</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://formacioncontinua.ufm.edu">Formación Continua</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://graduacion.ufm.edu">Graduaciones</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://heroes.ufm.edu">Héroes</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://laissezfaire.ufm.edu/">Laissez Faire</a></li>
    <li><a href="/Mapa_Campus" title="Mapa Campus">Mapa Campus</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://newmedia.ufm.edu">New Media</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.povertycure.org/">PovertyCure</a></li>
    <li><a href="/Tarifario_2019" title="Tarifario 2019">Tarifario 2019</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://wiki.ufm.edu/chh/index.php/Portada">Wiki diccionario</a></li></ul>
    </div>
    </div>

            </div>
            </div>
        </div>
        
        <div class="accordion-group">
            <div class="accordion-heading">
            <a class="accordion-toggle menucerrado" data-toggle="collapse" data-parent="#accordion2" href="#blogs">
                Blogs <i class="fa fa-arrow-down"></i>
            </a>
            </div>
            <div id="blogs" class="accordion-body collapse in">
            <div class="accordion-inner">
                <div class="row-fluid">
    <div class="span4 hidden-phone">
    <div class="row-fluid"><div class="span12" style="margin-top:10px; text-align:center; color:#808080;"><img src="/skins/Ufm/img/xnobleza3.png.pagespeed.ic.Dxml1DdkI_.webp" width="60%" style="margin-bottom:5px;"/><br/>La continua prueba de confianza que debemos dar a los demás en nuestra convivencia diaria.</div></div>
    </div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.exploraciones.ufm.edu/blog/">¿A quién pertenece el pasado?</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.cadep.ufm.edu/blog/">Centro para el Análisis de las Decisiones Públicas (CADEP)</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.cronica.ufm.edu/blog/">Crónica</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://bazar.ufm.edu/">El Foro y el Bazar</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://erasmus.ufm.edu/">Erasmus</a></li></ul>
    <p><br/>
    </p>
    </div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://librolibertate.wordpress.com/">Libro Libertate</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://naturalorder.ufm.edu/">Natural Order</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://escs.ufm.edu/pensarescrecer/">Pensar es Crecer</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://posgrado.ufm.edu/blog/">Praxis &amp; Lexis</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://nutricion.ufm.edu/blog/">Recetas y Salud</a></li></ul>
    </div>
    </div>

            </div>
            </div>
        </div>
        
        <div class="accordion-group">
            <div class="accordion-heading">
            <a class="accordion-toggle menucerrado" data-toggle="collapse" data-parent="#accordion2" href="#cultura">
                Cultura <i class="fa fa-arrow-down"></i>
            </a>
            </div>
            <div id="cultura" class="accordion-body collapse in">
            <div class="accordion-inner">
                <div class="row-fluid">
    <div class="span4 hidden-phone">
    <div class="row-fluid"><div class="span12" style="margin-top:10px; text-align:center; color:#808080;"><img src="/skins/Ufm/img/xsabiduria3.png.pagespeed.ic.SUB1MMMAzy.webp" width="70%" style="margin-bottom:5px;"/><br>Más que erudición, es sentido común para saber situarse y avanzar.</div></div>
    </div>
    <div class="span8">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.atlaslibertas.ufm.edu/">Atlas Libertas</a> </li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://casapopenoe.ufm.edu/">Casa Popenoe</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://conciertos.ufm.edu/">Departamento de Artes Escénicas</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://asomate.ufm.edu/">Eventos</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://lienzo.ufm.edu/">Lienzo Quauhquechollan</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://donquijote.ufm.edu/">Mooc Don Quijote Español</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://donquijote.ufm.edu/en">Mooc Don Quijote Inglés</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.popolvuh.ufm.edu">Museo Popol Vuh</a></li></ul>
    </div>
    </div>

            </div>
            </div>
        </div>
        
        <div class="accordion-group">
            <div class="accordion-heading">
            <a class="accordion-toggle menucerrado" data-toggle="collapse" data-parent="#accordion2" href="#ufm">
                UFM <i class="fa fa-arrow-down"></i>
            </a>
            </div>
            <div id="ufm" class="accordion-body collapse in">
            <div class="accordion-inner">
                <div class="row-fluid">
    <div class="span4 hidden-phone"><div class="row-fluid"><div class="span12" style="margin-top:10px; text-align:center; color:#808080;"><img src="/skins/Ufm/img/xcoraje3.png.pagespeed.ic.B5aLhnNuSK.webp" width="70%" style="margin-bottom:5px;"/><br/>La decisión y el valor de nuestras iniciativas.</div></div></div>
    <div class="span4">
    <ul><li><b><a href="/Alianzas" title="Alianzas">Alianzas</a></b></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://cuarenta.ufm.edu">Cuarenta años 1 misión</a></li>
    <li><a href="/Discurso_Inaugural" title="Discurso Inaugural">Discurso Inaugural Manuel F. Ayau</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/images/7/71/DiscursoInauguralLicMonterroso.pdf">Discurso del rector Fernando Monterroso</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/images/2/2e/DiscursoInauguralGiancarloIbarguen.pdf">Discurso del rector Giancarlo Ibárgüen</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/images/0/0e/DiscursoInauguralDrGabrielCalzada.pdf">Discurso del rector Gabriel Calzada</a></li>
    <li><a href="/Doctorados_Honoris_Causa" title="Doctorados Honoris Causa">Doctorados Honoris Causa</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://evolucion.ufm.edu">Evolución</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/images/d/d5/Excelencia.pdf">Excelencia</a></li></ul>
    </div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://fiduciarios.ufm.edu/">Fiduciarios</a></li>
    <li><a href="/Himno" title="Himno">Himno</a></li>
    <li><a href="/Ideario" title="Ideario">Ideario</a></li>
    <li><a href="/Informe_Financiero" title="Informe Financiero">Informe Financiero</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://cuarenta.ufm.edu/index.php/Linea_del_Tiempo">Línea del tiempo</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://muso.ufm.edu">Manuel F. Ayau</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://newmedia.ufm.edu/coleccion/proceso-economico-por-el-dr-manuel-ayau/por-que-la-ufm/">¿Por qué la UFM?</a></li>
    <li><a href="/Reglamentos" title="Reglamentos">Reglamentos</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/images/0/0e/Loa_Fco_Marroquin.pdf">Semblanza y Loa de Francisco</a> </li>
    <li><a href="/Tradiciones_UFM" title="Tradiciones UFM"> Tradiciones</a></li>
    <li><a href="/Tarifario_2019" title="Tarifario 2019">Tarifario 2019</a></li>
    <li><a href="/Valores" title="Valores">Valores</a> - <a href="/Virtudes" title="Virtudes">Virtudes</a></li></ul>
    </div>
    </div>

            </div>
            </div>
        </div>
        </div>  <!-- sidebar -->
    </div>
    <div id="container">
    <div id="content">
    <div id="header">
    <div class="hidden-phone">
        <div class="container">
        <div class="row">
            <div class="span3">
            <div style="padding:0;"> <a href="/index.php/"><img src="/skins/Ufm/img/xLogotipoUFM.png.pagespeed.ic.sNXIoCtJE_.webp"/></a> </div>
            </div>
            <div class="span9 topmenus">
            <div style="position: relative;" class="clearfix">
                <div class="row">
                <div class="social pull-right" style="">
                    <form class="navbar-form" style="margin:0;" id="searchform" method="GET" action="/Especial:Busqueda">
                    <div class="input-append" style="margin:0;">
                        <input name="q" class="input-small" type="text" style="-webkit-border-radius:0;-moz-border-radius:0;border-radius:0; margin:0; height:16px; ">
                        <button id="button_searchform" class="btn" type="button" style="-webkit-border-radius:0;-moz-border-radius:0;border-radius:0; height:26px;"><i class="icon-search" style="height:16px;"></i></button>
                    </div>
                    </form>
                </div>
                <div class="social pull-right" style="">
                    <div id="google_translate_element" style="text-align: right; padding-right:10px;"></div>
                    <script type="text/javascript">function googleTranslateElementInit(){new google.translate.TranslateElement({pageLanguage:'es',layout:google.translate.TranslateElement.InlineLayout.SIMPLE,autoDisplay:false,gaTrack:true,gaId:'UA-404175-1'},'google_translate_element');}</script><script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
                </div>
                </div>
            </div>
            <div class="sale_menu"></div>
            <div style="position:relative;" class="clearfix">
                <table id="menu-table" align="right" class="hidden-phone">
                <tr>
                    
                                                                <td class="solo">
                                                                    <div class="menu-key">
                                                                        <a href="/Estudios">Estudios</a>
                                                                    </div>
                                                                </td>
                                                                <td>
                                                                    <div class="menu-key" data-menu="facultades">
                                                                        Facultades
                                                                    </div>
                                                                </td>
                                                                <td>
                                                                    <div class="menu-key" data-menu="proyectos">
                                                                        Proyectos
                                                                    </div>
                                                                </td>
                                                                <td>
                                                                    <div class="menu-key" data-menu="recursos">
                                                                        Recursos
                                                                    </div>
                                                                </td>
                                                                <td>
                                                                    <div class="menu-key" data-menu="blogs">
                                                                        Blogs
                                                                    </div>
                                                                </td>
                                                                <td>
                                                                    <div class="menu-key" data-menu="cultura">
                                                                        Cultura
                                                                    </div>
                                                                </td>
                                                                <td>
                                                                    <div class="menu-key" data-menu="ufm">
                                                                        UFM
                                                                    </div>
                                                                </td>              </tr>
                </table>
            </div>
            </div>
        </div>
        </div>
    </div>
    </div>
    <div class="visible-phone">
    <div style="position:absolute; float:left;">
        <button type="button" class="btn toggle-sidebar"><i class="fa fa-bars fa-lg"></i></button>
    </div>
    <div style="padding:0; text-align:center; /*background:#d32e12;*/  "> <a href="/index.php/"><img src="/skins/Ufm/img/LogotipoUFM-top_rojo.png.pagespeed.ce.Jh46KSdFBs.png" style="width:250px;"/></a> </div>
    <div style="padding:35px 20px 10px 20px; text-align:center; color:#858585!important;"> <p>Nuestra <b>misión</b> es la enseñanza y difusión de los principios <b>éticos</b>, <b>jurídicos</b> y <b>económicos</b> de una sociedad de <b>personas</b> <b>libres</b> y <b>responsables</b>.
    </p> </div>
    <hr/>
    </div>

    <div class="container" style="margin-top:0px;">
    <div id="banner" class="hidden-phone">
        <div style="position:relative;">
        <div style="position:relative; ">
            <a href="" target="_blank"><img src="/images/c/c9/xPlantilla-foto-portal.jpg.pagespeed.ic.ZpwO2sdZ3E.webp"/></a>
            <div class="mycaption" style="position:absolute;right:0;top:0; ">
            <!--<div style="color:#fff; padding:9px; text-align:right; line-height:14px; color:#000; background:#00814A; opacity:0.9;"> <a href='https://twitter.com/hashtag/UFM45?src=hash' style="color:#fff;" >#UFM45</a></div>-->
            </div><!--caption-->
        </div>
        <div class="fondo_cita_posicion">
            <div class="row">
            <div class="span2">
                <div class="fondo_mycarousel" style="height:412px; width:250px; background:#00814A; color:#fff;">
                <!-- Carousel -->
                <div id="mycarousel" class="jcarousel-skin-ie7">
                    <ul>
                    </ul>
                </div>
                <div id="actual" style="display:none;">Actual</div>
                <!-- End Carousel -->
                <div id="loading_cita" style="display:none!important; position:absolute; top:-5px; color:#ccc; text-align:center; width:210px; padding:5px;">Cargando...<i class="fa fa-refresh fa-spin"></i></div>
                </div>
            </div>
            </div>
        </div><!--fondo-->
        </div><!--relativo-->
        <div id="menu_interno">
        
                        <div class="menu-value" data-menu="facultades">
                            <div class="menu-padding">
                                <div class="row-fluid">
    <div class="span4 hidden-phone"><div class="row-fluid"><div class="span12" style="margin-top:10px; text-align:center; color:#808080;"><img src="/skins/Ufm/img/xsabiduria3.png.pagespeed.ic.SUB1MMMAzy.webp" width="70%" style="margin-bottom:5px;"/><br>Más que erudición, es sentido común para saber situarse y avanzar.</div></div></div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://arquitectura.ufm.edu">Arquitectura</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://chh.ufm.edu">Centro Henry Hazlitt</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://fce.ufm.edu">Ciencias Económicas</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://escs.ufm.edu">Ciencias Sociales</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://derecho.ufm.edu">Derecho</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://educacion.ufm.edu">Educación</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://epri.ufm.edu">Estudios Políticos y Relaciones Internacionales</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://medicina.ufm.edu">Medicina</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://nutricion.ufm.edu">Nutrición</a></li></ul>
    </div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://odontologia.ufm.edu">Odontología</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://psicologia.ufm.edu">Psicología</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://actonmba.ufm.edu">Acton MBA</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://doctorado.ufm.edu">Programa de Doctorado</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://cine.ufm.edu/">Escuela de Cine y Artes Visuales</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://en.ufm.edu/">Escuela de Negocios</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://posgrado.ufm.edu/">Escuela de Posgrado</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://mpc.ufm.edu/">Michael Polanyi College</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://madrid.ufm.edu/">Campus Madrid</a></li></ul>
    </div>
    </div>

                            </div>
                        </div>
                        
                        <div class="menu-value" data-menu="proyectos">
                            <div class="menu-padding">
                                <div class="row-fluid">
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://antiguaforum.ufm.edu">Antigua Forum</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://arboretum.ufm.edu/">Arboretum</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://debates.ufm.edu/">Asociación de Debates</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://chh.ufm.edu">Centro Henry Hazlitt</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://doshistorias.ufm.edu/">Dos Historias, Una Ciudad</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://cadep.ufm.edu">Centro para el Análisis de las Deciones Públicas (CADEP)</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://hume.ufm.edu">Centro de Ética David Hume</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://capitalismo.ufm.edu/">Centro de Estudio del Capitalismo</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://centroik.ufm.edu">Centro Ibn Khaldun</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://fce.ufm.edu/inicio-cvs/">Centro Vernon Smith de Economía Experimental</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://cff.ufm.edu/2019/">College Freedom Forum At UFM 2019</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.stillman.ufm.edu/">Concurso Charles L. Stillman </a></li></ul>
    </div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://economia-austriaca.ufm.edu/">Congreso de Economía Austriaca</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://evolucion.ufm.edu/">Evolución</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://frc.ufm.edu/">Finance Research Center</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://gem.ufm.edu/">Global Entrepreneurship Monitor</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://grajedamena.ufm.edu/">Grajeda Mena</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.freedomsphilosopher.ufm.edu/index.php/Main_Page">Hayek Freedom's Philosopher</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://hazlitt.ufm.edu">Henry Hazlitt Archives</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://heuristica.ufm.edu">Heurística</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://jihu.ufm.edu">Jornadas de Investigación en Humanidades (JIHU)</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://fce.ufm.edu/kec/centro-de-emprendimiento-kirzner/">Kirzner Entrepreneurship Center</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://trends.ufm.edu/">Market Trends Es/En</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://donquijote.ufm.edu/">Mooc Don Quijote Es/En</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://salamanca.ufm.edu">Mooc La Escuela de Salamanca Es/En</a></li></ul>
    <p><br/>
    </p>
    </div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://opencourses.ufm.edu/courses/course-v1:Ciencia-Politica+CSESV1+2019/about">Mooc Capitalismo y Socialismo</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://opencourses.ufm.edu/courses/course-v1:Estudios-latinoamericanos+DMLES+2019/about">Mooc Dictaduras Militares Latinoamericanas</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://opencourses.ufm.edu">Open Courses</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.plazalibertad.ufm.edu">Plaza de la Libertad</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://pozoeconomico.ufm.edu">Pozo Económico</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://ita.ufm.edu">Programa ITA</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://grandeslibros.ufm.edu/">Seminario de Grandes Libros</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://semilladelibertad.ufm.edu/">Semilla de Libertad</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://escolasticos.ufm.edu">Sitio Escolástico</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://tedx.ufm.edu">TEDxUFM</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://hayek.ufm.edu">The Hayek Interviews</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://journal.apee.org">The Journal of Private Enterprise</a></li></ul>
    </div>
    </div>

                            </div>
                        </div>
                        
                        <div class="menu-value" data-menu="recursos">
                            <div class="menu-padding">
                                <div class="row-fluid">
    <div class="span4 hidden-phone"><div class="row-fluid"><div class="span12" style="margin-top:10px; text-align:center; color:#808080;"><img src="/skins/Ufm/img/xcoraje3.png.pagespeed.ic.B5aLhnNuSK.webp" width="70%" style="margin-bottom:5px;"/><br/>La decisión y el valor de nuestras iniciativas.</div></div></div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://alumni.ufm.edu/">Alumni</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://akademeia.ufm.edu/index.php/P%C3%A1gina_principal">Akademeia</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://arboretum.ufm.edu">Arboretum</a></li>
    <li><a href="/Asociaciones_Estudiantiles" title="Asociaciones Estudiantiles"> Asociación de Estudiantes</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://biblioteca.ufm.edu">Biblioteca</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://bookstore.ufm.edu">Bookstore</a></li>
    <li><a href="/Calendario_Acad%C3%A9mico_2019" title="Calendario Académico 2019">Calendario Académico 2019</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.ceta.ufm.edu">CETA</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://gt.creativecommons.org">Creative Commons</a></li>
    <li><a href="/Cr%C3%A9dito_Educativo" title="Crédito Educativo">Crédito Educativo</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://cronica.ufm.edu/">Crónica</a></li></ul>
    <p><br/>
    </p>
    </div>
    <div class="span4">
    <ul><li><a href="/Directorio" title="Directorio">Directorio</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://asomate.ufm.edu/">Eventos</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://formacioncontinua.ufm.edu">Formación Continua</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://graduacion.ufm.edu">Graduaciones</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://heroes.ufm.edu">Héroes</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://laissezfaire.ufm.edu/">Laissez Faire</a></li>
    <li><a href="/Mapa_Campus" title="Mapa Campus">Mapa Campus</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://newmedia.ufm.edu">New Media</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.povertycure.org/">PovertyCure</a></li>
    <li><a href="/Tarifario_2019" title="Tarifario 2019">Tarifario 2019</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://wiki.ufm.edu/chh/index.php/Portada">Wiki diccionario</a></li></ul>
    </div>
    </div>

                            </div>
                        </div>
                        
                        <div class="menu-value" data-menu="blogs">
                            <div class="menu-padding">
                                <div class="row-fluid">
    <div class="span4 hidden-phone">
    <div class="row-fluid"><div class="span12" style="margin-top:10px; text-align:center; color:#808080;"><img src="/skins/Ufm/img/xcoraje3.png.pagespeed.ic.B5aLhnNuSK.webp" width="70%" style="margin-bottom:5px;"/><br/>La decisión y el valor de nuestras iniciativas.</div></div>
    </div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.exploraciones.ufm.edu/blog/">¿A quién pertenece el pasado?</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.cadep.ufm.edu/blog/">Centro para el Análisis de las Decisiones Públicas (CADEP)</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.cronica.ufm.edu/blog/">Crónica</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://bazar.ufm.edu/">El Foro y el Bazar</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://erasmus.ufm.edu/">Erasmus</a></li></ul>
    <p><br/>
    </p>
    </div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://librolibertate.wordpress.com/">Libro Libertate</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://naturalorder.ufm.edu/">Natural Order</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://escs.ufm.edu/pensarescrecer/">Pensar es Crecer</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://posgrado.ufm.edu/blog/">Praxis &amp; Lexis</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://nutricion.ufm.edu/blog/">Recetas y Salud</a></li></ul>
    </div>
    </div>

                            </div>
                        </div>
                        
                        <div class="menu-value" data-menu="cultura">
                            <div class="menu-padding">
                                <div class="row-fluid">
    <div class="span4 hidden-phone">
    <div class="row-fluid"><div class="span12" style="margin-top:10px; text-align:center; color:#808080;"><img src="/skins/Ufm/img/xnobleza3.png.pagespeed.ic.Dxml1DdkI_.webp" width="60%" style="margin-bottom:5px;"/><br/>La continua prueba de confianza que debemos dar a los demás en nuestra convivencia diaria.</div></div>
    </div>
    <div class="span8">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.atlaslibertas.ufm.edu/">Atlas Libertas</a> </li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://casapopenoe.ufm.edu/">Casa Popenoe</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://conciertos.ufm.edu/">Departamento de Artes Escénicas</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://asomate.ufm.edu/">Eventos</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://lienzo.ufm.edu/">Lienzo Quauhquechollan</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://donquijote.ufm.edu/">Mooc Don Quijote Español</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://donquijote.ufm.edu/en">Mooc Don Quijote Inglés</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://www.popolvuh.ufm.edu">Museo Popol Vuh</a></li></ul>
    </div>
    </div>

                            </div>
                        </div>
                        
                        <div class="menu-value" data-menu="ufm">
                            <div class="menu-padding">
                                <div class="row-fluid">
    <div class="span4 hidden-phone"><div class="row-fluid"><div class="span12" style="margin-top:10px; text-align:center; color:#808080;"><img src="/skins/Ufm/img/xsabiduria3.png.pagespeed.ic.SUB1MMMAzy.webp" width="70%" style="margin-bottom:5px;"/><br>Más que erudición, es sentido común para saber situarse y avanzar.</div></div></div>
    <div class="span4">
    <ul><li><b><a href="/Alianzas" title="Alianzas">Alianzas</a></b></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://cuarenta.ufm.edu">Cuarenta años 1 misión</a></li>
    <li><a href="/Discurso_Inaugural" title="Discurso Inaugural">Discurso Inaugural Manuel F. Ayau</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/images/7/71/DiscursoInauguralLicMonterroso.pdf">Discurso del rector Fernando Monterroso</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/images/2/2e/DiscursoInauguralGiancarloIbarguen.pdf">Discurso del rector Giancarlo Ibárgüen</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/images/0/0e/DiscursoInauguralDrGabrielCalzada.pdf">Discurso del rector Gabriel Calzada</a></li>
    <li><a href="/Doctorados_Honoris_Causa" title="Doctorados Honoris Causa">Doctorados Honoris Causa</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://evolucion.ufm.edu">Evolución</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/images/d/d5/Excelencia.pdf">Excelencia</a></li></ul>
    </div>
    <div class="span4">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://fiduciarios.ufm.edu/">Fiduciarios</a></li>
    <li><a href="/Himno" title="Himno">Himno</a></li>
    <li><a href="/Ideario" title="Ideario">Ideario</a></li>
    <li><a href="/Informe_Financiero" title="Informe Financiero">Informe Financiero</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://cuarenta.ufm.edu/index.php/Linea_del_Tiempo">Línea del tiempo</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://muso.ufm.edu">Manuel F. Ayau</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://newmedia.ufm.edu/coleccion/proceso-economico-por-el-dr-manuel-ayau/por-que-la-ufm/">¿Por qué la UFM?</a></li>
    <li><a href="/Reglamentos" title="Reglamentos">Reglamentos</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/images/0/0e/Loa_Fco_Marroquin.pdf">Semblanza y Loa de Francisco</a> </li>
    <li><a href="/Tradiciones_UFM" title="Tradiciones UFM"> Tradiciones</a></li>
    <li><a href="/Tarifario_2019" title="Tarifario 2019">Tarifario 2019</a></li>
    <li><a href="/Valores" title="Valores">Valores</a> - <a href="/Virtudes" title="Virtudes">Virtudes</a></li></ul>
    </div>
    </div>

                            </div>
                        </div>
                            </div>
    </div><!--banner-->
    </div><!-- container con citas -->


    <!-- content -->
    <style>.btn-custom-darken.active{color:rgba(255,255,255,.75)}.btn-custom-darken{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,.25);background-color:#246ee4;background-image:-moz-linear-gradient(top,#3079ed,#135fd7);background-image:-webkit-gradient(linear,0 0,0 100%,from(#3079ed),to(#135fd7));background-image:-webkit-linear-gradient(top,#3079ed,#135fd7);background-image:-o-linear-gradient(top,#3079ed,#135fd7);background-image:linear-gradient(to bottom,#3079ed,#135fd7);background-repeat:repeat-x;filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff3079ed', endColorstr='#ff135fd7', GradientType=0);border-color:#135fd7 #135fd7 #0d4091;border-color:rgba(0,0,0,.1) rgba(0,0,0,.1) rgba(0,0,0,.25);*background-color: #135fd7;filter: progid:DXImageTransform.Microsoft.gradient(enabled = false)}.btn-custom-darken:hover,.btn-custom-darken:focus,.btn-custom-darken:active,.btn-custom-darken.active,.btn-custom-darken.disabled,.btn-custom-darken[disabled]{color:#fff;background-color:#135fd7;*background-color: #1154c0}.btn-custom-darken:active,.btn-custom-darken.active{background-color:#0f4aa8}.masinfologin{line-height:5px!important;font-size:12px!important}.medios a{font-weight:bold;color:#08c!important}ul.enmedios{margin:0}ul.enmedios li{list-style:none;padding:4px 0}div.dsuperior{padding-top:18px}div.dsuperior ul{margin:0}div.dsuperior ul li{list-style:none;padding:0}div.dsuperior ul li a{font-size:.9em}.medios_titulo{color:#d32e12;text-align:left!important;font-size:1.2em}</style>
    <!-- container --> 
    <div class="container">
        <div class="row" style="margin-top:5px;">
            <div class="span3">
                <div style="padding:0;">
                    <div id="login">
                        <form id="formufm" method="post">
                        <p>
                            <div style='padding-top:8px; padding-bottom:5px; font-size:0.95em;'>Iniciar sesión con Google</div> 
                            <a href="https://accounts.google.com/o/oauth2/auth?response_type=code&access_type=online&client_id=753553871119-42rgfeitjhbrq449nj1906662pupr1j0.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fwww.ufm.edu%2Fautenticacion%2Foauth2_init.php&state=22b358f4d763c315101f09e5b02c2c44&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&approval_prompt=auto&hd=ufm.edu" id="ufmail_" style="padding:5px 16px;" class="btn btn-custom-darken">UFMail</a> 
                            <!--<button type="button" class="btn btn-custom-darken" data-toggle="modal" data-target="#myModal2">MiU</button>-->
                            <a href="https://accounts.google.com/o/oauth2/auth?response_type=code&access_type=offline&client_id=514583071787-mcsoogoa3kb7v56n7r78obvusehc81br.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fmiu.ufm.edu%2Findex.php&state=ebea172449a27f64ae4ec6341c028504&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&approval_prompt=force&hd=ufm.edu&login_hint=ejemplo%40ufm.edu" id="miu_" style="padding:5px 16px;;" class="btn btn-custom-darken">MiU</a>
                        </p>
                        </form>
                    </div>
                </div>
                <div class="visible-phone">
                    <hr/>
                </div>
            </div>  

            <div class="hidden-phone">
            <!--<div class='span4'>-->
            <div class="span2">
    <div class="dsuperior">
    <ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/english/">UFM Key Projects</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://foufm.org">Friends of UFM</a></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ufm.edu/checkout/donaciones/">Donaciones</a></li>
    <li><a href="/Especial:Sugerencias" title="Especial:Sugerencias"> Contáctenos</a></li></ul>
    </div>
    </div>
    <div class="span2">
    <div class="dsuperior">
    <ul><li><b><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="http://admisiones.ufm.edu/">Admisiones</a></b></li>
    <li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://alumni.ufm.edu/">Alumni</a></li>
    <li><b><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://madrid.ufm.edu/?referer=ufm">Campus Madrid</a></b></li>
    <li><a href="/Redes_Sociales" title="Redes Sociales"> Redes Sociales</a></li></ul>
    </div>
    </div>
            <!--</div>-->
            </div>
            
            <div class="span5">
                <div class="mision hidden-phone" style="padding: 0;">
                    <br/>
                    <p>Nuestra <b>misión</b> es la enseñanza y difusión de los principios <b>éticos</b>, <b>jurídicos</b> y <b>económicos</b> de una sociedad de <b>personas</b> <b>libres</b> y <b>responsables</b>.
    </p>        	</div>
            </div>
        </div>    

        <hr style="margin: 10px 0!important;"/>
            
        <div class="row">          
            <div>
                
                <div class="span3 div_noticias">
                <div class="elemento">
                    <div class="text-right seccion_titulo "><small><a href="https://noticias.ufm.edu" target="_blank" title="El Amigo de la Marro">El Amigo de la Marro</a></small></div><div data-index="1" data-category="noticias" class="imagen " style="text-align:center;"><a href="https://noticias.ufm.edu/stephanie-falla-entre-las-50-mujeres-mas-desafiantes-de-centro-america/" target="_blank"><img src="//www.ufm.edu/skins/Ufm/plugins/RssCitasFondos/img/x1568912628_thumb_snoticiaswpcontentuploads201909stepnegociosthumb.png.pagespeed.ic.f-GTkBf5dg.webp"/></a></div><div data-index="2" data-category="noticias" class="imagen hidden" style="text-align:center;"><a href="https://noticias.ufm.edu/medicina-ufm-celebro-xv-aniversario-del-centro-de-salud-barbara/" target="_blank"><img src="//www.ufm.edu/skins/Ufm/plugins/RssCitasFondos/img/x1568912628_thumb_snoticiaswpcontentuploads201909decanocsbthumb.png.pagespeed.ic.fv2az2rSTa.webp"/></a></div><div data-index="3" data-category="noticias" class="imagen hidden" style="text-align:center;"><a href="https://noticias.ufm.edu/participa-en-la-alumni-fest-en-la-ufm/" target="_blank"><img src="//www.ufm.edu/skins/Ufm/plugins/RssCitasFondos/img/x1568912628_thumb_snoticiaswpcontentuploads201909alumnifestthumb.png.pagespeed.ic.hBXu1G9RLK.webp"/></a></div><div data-index="1" data-category="noticias" class="titulo active item_titulo"><small><a href="https://noticias.ufm.edu/stephanie-falla-entre-las-50-mujeres-mas-desafiantes-de-centro-america/" target="_blank">Stephanie Falla entre las 50 mujeres más desafiantes de Centro América</a></small></div><div data-index="2" data-category="noticias" class="titulo  item_titulo"><small><a href="https://noticias.ufm.edu/medicina-ufm-celebro-xv-aniversario-del-centro-de-salud-barbara/" target="_blank">Medicina UFM celebró XV aniversario del Centro de Salud Bárbara</a></small></div><div data-index="3" data-category="noticias" class="titulo  item_titulo"><small><a href="https://noticias.ufm.edu/participa-en-la-alumni-fest-en-la-ufm/" target="_blank">¡Participa en el Alumni Fest UFM!</a></small></div>
                </div>
            </div>
            <div class="span3 div_eventos">
                <div class="elemento">
                <div class="text-right seccion_titulo "><small><a href="https://asomate.ufm.edu" target="_blank" title="Eventos">Eventos</a></small></div><div data-index="1" data-category="asómate" class="imagen "><a href="https://asomate.ufm.edu/event/curso-libre-conceptos-clave-pensamiento-tocqueville/" target="_blank"><img src="//www.ufm.edu/skins/Ufm/plugins/RssCitasFondos/img/x1568912628_thumb_sasomatewpcontentuploads201908asomate_tocqueville.png.pagespeed.ic.JlIDGvPMe5.webp"></a></div><div data-index="2" data-category="asómate" class="imagen hidden"><a href="https://asomate.ufm.edu/event/las-mujeres-arte-guatemalteco/" target="_blank"><img src="//www.ufm.edu/skins/Ufm/plugins/RssCitasFondos/img/x1568912628_thumb_sasomatewpcontentuploads201908bannerwebufm0101.png.pagespeed.ic.0kttt1RyyA.webp"></a></div><div data-index="3" data-category="asómate" class="imagen hidden"><a href="https://asomate.ufm.edu/event/1615/" target="_blank"><img src="//www.ufm.edu/skins/Ufm/plugins/RssCitasFondos/img/x1568912628_thumb_sasomatewpcontentuploads201908htmlartemodernoufm3modulos021.png.pagespeed.ic.6q0fXtWeMG.webp"></a></div><div data-index="1" data-category="asómate" class="titulo active item_titulo"><small><a href="https://asomate.ufm.edu/event/curso-libre-conceptos-clave-pensamiento-tocqueville/" target="_blank">Curso libre: Conceptos Clave en el Pensamiento de Tocqueville</a></small></div><div data-index="2" data-category="asómate" class="titulo  item_titulo"><small><a href="https://asomate.ufm.edu/event/las-mujeres-arte-guatemalteco/" target="_blank">Las Mujeres en el Arte Guatemalteco</a></small></div><div data-index="3" data-category="asómate" class="titulo  item_titulo"><small><a href="https://asomate.ufm.edu/event/1615/" target="_blank">Cursos libres: Historia del Arte Moderno</a></small></div>
                </div>
            </div>
            <div class="span3 div_videos">
                <div class="elemento">
                    <div class="text-right seccion_titulo "><small><a href="https://newmedia.ufm.edu" target="_blank" title="Newmedia">Newmedia</a></small></div><div data-index="1" data-category="videos" class="imagen "><a href="https://newmedia.ufm.edu/video/ricardo-gomes-oportunidades-para-la-politica-liberal-en-brasil/" target="_blank"><img src="//www.ufm.edu/skins/Ufm/plugins/RssCitasFondos/img/x1568912628_thumb_snewmediawpcontentuploads201909ricardo_gomes.png.pagespeed.ic.7zuKXz8b-N.webp"></a></div><div data-index="2" data-category="videos" class="imagen hidden"><a href="https://newmedia.ufm.edu/video/first-tuesday-ufm-el-arte-del-buen-vestir/" target="_blank"><img src="//www.ufm.edu/skins/Ufm/plugins/RssCitasFondos/img/x1568912628_thumb_snewmediawpcontentuploads201909firsttuesday_buenvestir.png.pagespeed.ic.d0ELe0rK7j.webp"></a></div><div data-index="3" data-category="videos" class="imagen hidden"><a href="https://newmedia.ufm.edu/video/homenaje-especial-en-honor-de-armando-de-la-torre/" target="_blank"><img src="//www.ufm.edu/skins/Ufm/plugins/RssCitasFondos/img/x1568912628_thumb_snewmediawpcontentuploads201909homenaje_armandodelatorre.png.pagespeed.ic.0V7fSZR-x1.webp"></a></div><div data-index="1" data-category="videos" class="titulo active item_titulo"><small><a href="https://newmedia.ufm.edu/video/ricardo-gomes-oportunidades-para-la-politica-liberal-en-brasil/" target="_blank">Ricardo Gomes, oportunidades para la política liberal en Brasil</a></small></div><div data-index="2" data-category="videos" class="titulo  item_titulo"><small><a href="https://newmedia.ufm.edu/video/first-tuesday-ufm-el-arte-del-buen-vestir/" target="_blank">First Tuesday UFM: El arte del buen vestir</a></small></div><div data-index="3" data-category="videos" class="titulo  item_titulo"><small><a href="https://newmedia.ufm.edu/video/homenaje-especial-en-honor-de-armando-de-la-torre/" target="_blank">Homenaje especial en honor de Armando de la Torre</a></small></div>
                </div>
            </div>
                <div class="span3 div_noticias">
                    <div class="elemento">
                        <div class="text-right seccion_titulo medios"><small><a href="https://noticias.ufm.edu/category/UFM-medios/" target="_blank" title="UFM en medios">UFM en medios</a></small></div><div data-index="1" data-category="ufm en medios" class="imagen " style="text-align:center;"><a href="https://noticias.ufm.edu/bronzelens-film-festival-selecciono-cortometraje-de-pedro-pablo-herrera/" target="_blank"><img src="//www.ufm.edu/skins/Ufm/plugins/RssCitasFondos/img/x1568912628_thumb_snoticiaswpcontentuploads201907ppcinethumb.png.pagespeed.ic.tUopk7I4WN.webp"/></a></div><div data-index="2" data-category="ufm en medios" class="imagen hidden" style="text-align:center;"><a href="https://noticias.ufm.edu/luis-zelaya-the-lawyer-magazine/" target="_blank"><img src="//www.ufm.edu/skins/Ufm/plugins/RssCitasFondos/img/x1568912628_thumb_snoticiaswpcontentuploads201906luchozelayathumb.png.pagespeed.ic.eF4HD_b_gt.webp"/></a></div><div data-index="3" data-category="ufm en medios" class="imagen hidden" style="text-align:center;"><a href="https://noticias.ufm.edu/cosmides-tooby-recibieron-doctorados-honorificos-la-ufm/" target="_blank"><img src="//www.ufm.edu/skins/Ufm/plugins/RssCitasFondos/img/x1568912628_thumb_snoticiaswpcontentuploads201905cosmidestoobythumb.png.pagespeed.ic.OzwG8m_Cui.webp"/></a></div><div data-index="1" data-category="ufm en medios" class="titulo active item_titulo"><small><a href="https://noticias.ufm.edu/bronzelens-film-festival-selecciono-cortometraje-de-pedro-pablo-herrera/" target="_blank">BronzeLens Film Festival seleccionó cortometraje de Pedro Pablo Herrera</a></small></div><div data-index="2" data-category="ufm en medios" class="titulo  item_titulo"><small><a href="https://noticias.ufm.edu/luis-zelaya-the-lawyer-magazine/" target="_blank">Luis Zelaya en The Lawyer Magazine</a></small></div><div data-index="3" data-category="ufm en medios" class="titulo  item_titulo"><small><a href="https://noticias.ufm.edu/cosmides-tooby-recibieron-doctorados-honorificos-la-ufm/" target="_blank">Cosmides y Tooby recibieron doctorados honoríficos en la UFM</a></small></div>
                    </div>
                </div>		</div>
        </div>	

        <div class="row">          
            <div class="span12">
                <br/>
            </div>
        </div>	


    <!-- container --> 

    <script type="text/javascript" async>var index=0;var category=0;var e=0;jQuery('div.titulo').hover(function(){index=jQuery(this).data('index');category=jQuery(this).data('category');if(index!=1){e=jQuery('div.imagen[data-index="'+index+'"][data-category="'+category+'"]');jQuery('div.imagen[data-index="1"][data-category="'+category+'"]').addClass('hidden');e.removeClass('hidden');jQuery('div.titulo[data-index="1"][data-category="'+category+'"]').removeClass('active');jQuery(this).addClass('active');}},function(){if(index!=1){jQuery('div.imagen[data-index="1"][data-category="'+category+'"]').removeClass('hidden');e.addClass('hidden');jQuery('div.titulo[data-index="1"][data-category="'+category+'"]').addClass('active');jQuery(this).removeClass('active');}});function mycarousel_initCallback(carousel){jQuery('#actual').bind('click',function(){carousel.scroll(jQuery.jcarousel.intval(457));return false;});};function mycarousel_itemLoadCallback(carousel,state){if(carousel.has(carousel.first,carousel.last)){mitotal=457;first=carousel.first;if(first==mitotal){jQuery('#actual').hide();}if(first<mitotal){jQuery('#actual').show();}jQuery('#loading_cita').fadeOut('fast');return false;}else{jQuery('#loading_cita').fadeIn('fast');jQuery('#actual').fadeOut('fast');jQuery.get('//www.ufm.edu/skins/Ufm/plugins/RssCitasFondos/citas_ajax_xml.php',{first:carousel.first,last:carousel.last},function(xml){jQuery('#loading_cita').fadeOut('fast');mycarousel_itemAddCallback(carousel,carousel.first,carousel.last,xml);},'xml');}};function mycarousel_itemAddCallback(carousel,first,last,xml){mitotal=457;if(first<mitotal){jQuery('#actual').fadeIn('fast');}carousel.size(parseInt(jQuery('total',xml).text()));jQuery('image',xml).each(function(i){carousel.add(first+i,mycarousel_getItemHTML(jQuery(this).text()));});};function mycarousel_getItemHTML(url){return'<div style="padding:5px 10px 5px 10px;">'+url+'</div>';};jQuery(document).ready(function(){jQuery('#actual').hide();jQuery('#mycarousel').jcarousel({itemLoadCallback:mycarousel_itemLoadCallback,initCallback:mycarousel_initCallback,scroll:1,start:457});});</script>

    <script type="text/javascript">(function(a,e,c,f,g,h,b,d){var k={ak:"1000881927",cl:"ox-rCIuby3sQh_6g3QM",autoreplace:"(+502) 2338-7700"};a[c]=a[c]||function(){(a[c].q=a[c].q||[]).push(arguments)};a[g]||(a[g]=k.ak);b=e.createElement(h);b.async=1;b.src="//www.gstatic.com/wcm/loader.js";d=e.getElementsByTagName(h)[0];d.parentNode.insertBefore(b,d);a[f]=function(b,d,e){a[c](2,b,k,d,null,new Date,e)};a[f]()})(window,document,"_googWcmImpl","_googWcmGet","_googWcmAk","script");</script>

    <!-- Modal -->
    <!--
    <div class="modal fade" id="myModal2" tabindex="-1" role="dialog" aria-labelledby="myModal2Label">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h2>MiU</h2>
        </div>
        <div class="modal-body">
                        MiU se encuentra en mantenimiento. <br/><br/>
                        
                        Gracias por su comprensión.<br/>
                        ¡Regresaremos pronto!	
        </div>
        </div>
    </div>
    </div>
    --><!--footer_page-->
    <div id="push"></div>
    </div>
    <!--frame-->

            <div id="footer">
            <!-- footer -->
                <div class="hidden-phone">
                    <div class="container">
                        <div style="height:3px;background:#e41220;"></div>
                        <div class="row" style="padding-top:20px;">
                            <div class="span12">
                                <div class="row-fluid" style="margin-top:-5px;">
                                    <div class="span4">
                                        <strong>Universidad Francisco Marroquín</strong>
                                        <br>
                                        <a href="#myModal" data-toggle="modal">Calle Manuel F. Ayau <span style="font-size:10px;">(6 Calle final),</span> zona 10</a>
                                        <br>
                                        Guatemala, Guatemala 01010
                                    </div>
                                    <div class="span4">
                                        Teléfono: <a href='tel:+50223387700'>(+502) 2338-7700</a>
                                        <br>
                                        Fax: (+502) 2334-6896
                                        <br>
                                        <a href="mailto:inf@ufm.edu" style="color:#333;">inf@ufm.edu</a> |&nbsp; <a href="mailto:webmaster@ufm.edu" style="color:#333;">webmaster@ufm.edu</a>
                                                                            
                                    </div>
                                    <div class="span4">
                                            <span style="font-size:1.6em;">
                                            <a href="http://www.linkedin.com/edu/school?id=12868&trk=tyah&trkInfo=tas%3Auniversidad%20francisco%20marroqu%EDn%2Cidx%3A3-1-4" target="_blank"><i class="fa fa-linkedin-square"></i></a>
                                            <a href="https://www.facebook.com/UFMedu" target="_blank"><i class="fa fa-facebook-square"></i></a>
                                            <a href="https://twitter.com/ufmedu" target="_blank"><i class="fa fa-twitter-square"></i></a>
                                            <a href="https://plus.google.com/u/0/+UFMedu/posts" target="_blank"><i class="fa fa-google-plus-square "></i></a>
                                            <a href="http://www.youtube.com/user/newmediaufm?feature=watch" target="_blank"><i class="fa fa-youtube"></i></a>
                                            <a href="http://www.pinterest.com/ufmedu/boards/" target="_blank"><i class="fa fa-pinterest-square"></i></a>
                                            <span style="position: relative;" class="elshare">
                                            <a href="#" class="myshare" title="Compartir"><i style="cursor:pointer;" class="fa fa-share-alt-square"></i></a>
                                            <div style="display:none; position: absolute; font-size:20px; padding:0 5px; margin-top:2px; z-index:1000; background:#f1f1f1; width:100px; text-align:left; " class="social_color pull-right listaredes">
                                                <a href="http://www.facebook.com/sharer.php?u=https://ww1.ufm.edu/&t=Universidad%20Francisco%20Marroquín" target="_blank"><i class="fa fa-facebook-square"></i> <span style="font-size:12px;">Facebook</span></a><br/>
                                                <a href="http://twitter.com/home?status=Universidad%20Francisco%20Marroquín,%20https://ww1.ufm.edu/" target="_blank"><i class="fa fa-twitter-square"></i> <span style="font-size:12px;">Twitter</span></a> <br/>
                                                <a href="http://www.linkedin.com/shareArticle?mini=true&url=https://ww1.ufm.edu&title=Universidad%20Francisco%20Marroqu%C3%ADn" target="_blank"><i class="fa fa-linkedin-square"></i> <span style="font-size:12px;">Linkedin</span></a><br/>
                                            </div>
                                            </span>
                                            | <a href="#" onclick="ps2O8pow(); return false;" class="" title="Soporte en línea"><i class="fa fa-comments-o" aria-hidden="true"></i></a>										
                                            </span><br/>
                                        &copy; 1998 Universidad Francisco Marroquín&nbsp; | <a target="_blank" style="text-decoration:none;" rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/gt/" title="Este obra está bajo una Licencia Creative Commons Atribución-NoComercial-CompartirIgual 3.0 Guatemala.">CC: BY-NC-SA</a>&nbsp;<br/>									
                                        <!--<img alt="Licencia Creative Commons" src="/skins/Ufm/img/80x15a.png">-->
                                        <a href="https://www.ufm.edu/Aviso_Legal" target="_blank">Aviso Legal</a> - <a href="https://www.ufm.edu/Política_de_Cookies" target="_blank">Política de cookies</a> - <a href="https://www.ufm.edu/Políticas_de_privacidad" target="_blank">Política de privacidad</a>									
                                    </div>                            
                                </div>

                            </div>
                        </div>
                    </div>
                </div>

    <!-- BEGIN ProvideSupport.com Graphics Chat Button Code -->
    <div id="sc2O8p" style="display: none;"></div>
    <div id="sd2O8p" style="display: none;"></div>
    <script type="text/javascript">var se2O8p=document.createElement("script");se2O8p.type="text/javascript";var se2O8ps=(location.protocol.indexOf("https")==0?"https":"http")+"://image.providesupport.com/js/ufmmiu/safe-standard.js?ps_h=2O8p&ps_t="+new Date().getTime();setTimeout("se2O8p.src=se2O8ps;document.getElementById('sd2O8p').appendChild(se2O8p)",1);</script>
    <noscript>
        <div style="display:inline">
            <a href="http://www.providesupport.com?messenger=ufmmiu">Online Chat</a>
        </div>
    </noscript>
    <!-- END ProvideSupport.com Graphics Chat Button Code -->


                
                <!-- footer -->
                <div class="visible-phone" style="margin-top:100px; ">
                    <div class="container" style="text-align:center;">
                        
                        <div class="row">
                            <div style="height:60px;text-align:center; margin-bottom:70px; position:relative; background:#e41220;">
                                <img style="margin:10px auto; width:120px;" src="/skins/Ufm/img/LogotipoUFM-footer.png.pagespeed.ce.ckYu8soHWG.png"/>    						
                            </div>
                        </div>
                        <div class="row">
                        <strong>Universidad Francisco Marroquín</strong>
                        <br>
                        <a href="#myModal" data-toggle="modal">Calle Manuel F. Ayau <span style="font-size:10px;">(6 Calle final),</span> zona 10</a>
                        <br>
                        Guatemala, Guatemala 01010
                        <br>
                        Teléfono: (+502) 2338-7700
                        <br>
                        Fax: (+502) 2334-6896
                        <br>
                        <a href="mailto:inf@ufm.edu" style="color:#333;">inf@ufm.edu</a> | <a href="mailto:webmaster@ufm.edu" style="color:#333;">webmaster@ufm.edu</a>
                        </div>
                        <div class="row">
                        <div class="social">	                    
                            <a href="http://www.linkedin.com/edu/school?id=12868&trk=tyah&trkInfo=tas%3Auniversidad%20francisco%20marroqu%EDn%2Cidx%3A3-1-4" target="_blank"><i class="fa fa-linkedin-square"></i></a>
                            <a href="https://www.facebook.com/UFMedu" target="_blank"><i class="fa fa-facebook-square"></i></a>
                            <a href="https://twitter.com/ufmedu" target="_blank"><i class="fa fa-twitter-square"></i></a>
                            <a href="http://www.youtube.com/user/newmediaufm?feature=watch" target="_blank"><i class="fa fa-youtube-play"></i></a>
                            <a href="http://www.pinterest.com/ufmedu/boards/" target="_blank"><i class="fa fa-pinterest-square"></i></a>
                            
                            <span style="position: relative;" class="elshare">
                            <a href="#" class="myshare" title="Compartir"><i style="cursor:pointer;" class="fa fa-share-alt-square"></i></a>
                            <div style="display:none; position: absolute; font-size:20px; padding:0 5px; margin-top:2px; z-index:1000; top:-80px; background:#f1f1f1; width:100px; text-align:left; " class="social_color pull-right listaredes">
                                <a href="http://www.facebook.com/sharer.php?u=https://www.ufm.edu/index.php/Portal&t=Portal" target="_blank"><i class="fa fa-facebook-square"></i> <span style="font-size:12px;">Facebook</span></a><br/>
                                <a href="http://twitter.com/home?status=Portal,%20https://www.ufm.edu/index.php/Portal" target="_blank"><i class="fa fa-twitter-square"></i> <span style="font-size:12px;">Twitter</span></a> <br/>
                                <a href="http://www.linkedin.com/shareArticle?mini=true&url=https://www.ufm.edu&title=Universidad%20Francisco%20Marroqu%C3%ADn" target="_blank"><i class="fa fa-linkedin-square"></i> <span style="font-size:12px;">Linkedin</span></a><br/>
                            </div>
                            </span>

                            <!-- BEGIN ProvideSupport.com Graphics Chat Button Code -->
                            <div id="sc2O8p" style="display: none;"></div>
                            <div id="sd2O8p" style="display: none;"></div>
                            <script type="text/javascript">var se2O8p=document.createElement("script");se2O8p.type="text/javascript";var se2O8ps=(location.protocol.indexOf("https")==0?"https":"http")+"://image.providesupport.com/js/ufmmiu/safe-standard.js?ps_h=2O8p&ps_t="+new Date().getTime();setTimeout("se2O8p.src=se2O8ps;document.getElementById('sd2O8p').appendChild(se2O8p)",1);</script>
                            <noscript>
                                <div style="display:inline">
                                    <a href="http://www.providesupport.com?messenger=ufmmiu">Online Chat</a>
                                </div>
                            </noscript>
                            <!-- END ProvideSupport.com Graphics Chat Button Code -->
                            | <a href="#" onclick="ps2O8pow(); return false;" class="" title="Soporte en línea"><i class="fa fa-comments-o" aria-hidden="true"></i></a>
                                                                            
                        </div>
                        </div>
                        <div class="row">
                                        <a href="https://www.ufm.edu/index.php/Mapa_Campus" target="_blank">Mapa del campus</a> | &copy; - 1998 Universidad Francisco Marroquín&nbsp; <br/>
                        <a target="_blank" style="text-decoration:none;" rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/gt/" title="Este obra está bajo una Licencia Creative Commons Atribución-NoComercial-CompartirIgual 3.0 Guatemala.">CC: BY-NC-SA</a>&nbsp;<br/>
                                        <a href="https://www.ufm.edu/Aviso_Legal" target="_blank">Aviso Legal</a> - <a href="https://www.ufm.edu/Política_de_Cookies" target="_blank">Política de cookies</a> - <a href="https://www.ufm.edu/Políticas_de_privacidad" target="_blank">Política de privacidad</a>									

                        </div>
                    </div>
                </div>
            <!-- footer -->
            </div>


        <div id="myModal" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
            <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
            <h3 id="myModalLabel">Universidad Francisco Marroquín</h3>
            </div>
            <div class="modal-body">
            <a href="https://www.ufm.edu/index.php/Mapa_Campus" target="_blank"><img src="/skins/Ufm/img/xgooglemaps-ufm.jpg.pagespeed.ic.uasdwaZEEU.webp"/></a>
            </div>
            <div class="modal-footer">
            <button class="btn" data-dismiss="modal" aria-hidden="true">Cerrar</button>      
            </div>
        </div>		
        </body>
    </html><script>(window.RLQ=window.RLQ||[]).push(function(){mw.loader.load(["mediawiki.action.view.postEdit","site","mediawiki.user","mediawiki.hidpi","mediawiki.page.ready","mediawiki.searchSuggest"]);});</script><script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgBackendResponseTime":355});});</script>
    """
soup = BeautifulSoup(html_doc,'html.parser')
title = soup.title.string
meta = soup.find_all("meta",limit = 8)
for i in meta:
    si = str(i)
    if si == '<meta content="https://www.ufm.edu" property="og:url"/>':
        link_line = BeautifulSoup(si,'html.parser')
link_attrs = link_line.meta
link_name = link_attrs['content']


link_tag = soup.find_all("link")
# print("")
# print("hrefs are: ")

for i in link_tag :
    # print("---------------------------------------------------------------------------------------------------")
    # print("   - ",i['href'])
    pass

a_tag = soup.find_all("a")
for i in a_tag :
    # print("---------------------------------------------------------------------------------------------------")
    # print("   - ",i['href'])
    no = str(i)
    if no == '<a href="mailto:inf@ufm.edu" style="color:#333;">inf@ufm.edu</a>':
        mail_line = BeautifulSoup(no,'html.parser')
mail_attrs = mail_line.a
mail_name = mail_attrs['href']

dd = '''<a href='tel:+50223387700'>(+502) 2338-7700</a>'''

for i in a_tag :
    if i['href'] =="tel:+50223387700":
        number_name = i['href']



# number_attrs = number_line.a
# number_name = number_attrs['href']
# print (number_name)

print("")
print("< Fabricio Juarez >")
print("")
print("1.portal")
print ("        title is: ",title)   
print("")
print ("        mail is: ",mail_name)
print("")
print ("        adress is: ",link_name)   
print("")
print ("       ",number_name)   


        
