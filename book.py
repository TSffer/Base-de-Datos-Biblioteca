#!C:\Python27\python

import cgi
import cgitb; cgitb.enable()
import mysql.connector
import re

print("Content-Type: text/html\n")

dato = {'user' : 'root',
        'password':'',
        'database':'biblioteca',
        'host':'127.0.0.1'}
db = mysql.connector.connect(** dato)

form = cgi.FieldStorage()
codigo_corretativo = form.getfirst('codigoCorrelativo','empty')
categoria = form.getfirst('categoria','empty')
titulo = form.getfirst('titulo','empty')
autor = form.getfirst('autor','empty')
pais = form.getfirst('pais','empty')
editorial = form.getfirst('editorial','empty')
edicion = form.getfirst('edicion','empty')
estado = form.getfirst('estado','empty')

if(codigo_corretativo!="empty" and categoria!="empty" and titulo!="empty" and autor!="empty" and pais!="empty" and editorial!="empty" and edicion!="empty" and estado!="empty" ):
    insertar = db.cursor()
    cursor = db.cursor()
    cursor1 = db.cursor()
    cursor2 = db.cursor()  #Ya se que basta con uno solo
    cursor3 = db.cursor()
    cursor4 = db.cursor()
    insertar.execute("insert into soportlibro values(null,'%s')" % (estado))
    db.commit()
    cursor.execute("select soportLibro_Id from soportlibro where soportLibro_Id = (select max(soportLibro_Id) from soportlibro)")
    resultado = cursor.fetchall()
    s_id = resultado[0][0]
    cursor1.execute("select administrador_Id from administrador where administrador_Id = (select max(administrador_Id) from administrador)")
    resultado1 = cursor1.fetchall()
    a_id = resultado1[0][0]
    insertar.execute("insert into recurso values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (codigo_corretativo,categoria,titulo,autor,pais,editorial,edicion,estado,s_id,a_id))
    db.commit()
    cursor2.execute("insert into estado values(null,'%s')"%(estado))
    db.commit()
    cursor3.execute("select estado_Id from estado where estado_Id = (select max(estado_Id) from estado)")
    resultadoE = cursor3.fetchall()
    He = resultadoE[0][0]
    cursor4.execute("select recurso_Id from recurso where recurso_Id = (select max(recurso_Id) from recurso)")
    resultadoR = cursor4.fetchall()
    RI = resultadoR[0][0]
    insertar.execute("insert into historico_estado values(null,'%s','%s',CURRENT_TIMESTAMP)" % (RI,He))
    db.commit()
    insertar.close()
    cursor.close()
    cursor1.close()
    cursor3.close()
    cursor4.close()
print("""

<!DOCTYPE html>
<html lang="es">
<head> 
    <title>Registrar Libro</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="Shortcut Icon" type="image/x-icon" href="assets/icons/book.ico" />
    <script src="js/sweet-alert.min.js"></script>
    <link rel="stylesheet" href="css/sweet-alert.css">
    <link rel="stylesheet" href="css/material-design-iconic-font.min.css">
    <link rel="stylesheet" href="css/normalize.css">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/jquery.mCustomScrollbar.css">
    <link rel="stylesheet" href="css/style.css">
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="js/jquery-1.11.2.min.js"><\/script>')</script>
    <script src="js/modernizr.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/jquery.mCustomScrollbar.concat.min.js"></script>
    <script src="js/main.js"></script>
</head>
<body>
    <div class="navbar-lateral full-reset">
        <div class="visible-xs font-movile-menu mobile-menu-button"></div>
        <div class="full-reset container-menu-movile custom-scroll-containers">
            <div class="logo full-reset all-tittles">
                <i class="visible-xs zmdi zmdi-close pull-left mobile-menu-button" style="line-height: 55px; cursor: pointer; padding: 0 10px; margin-left: 7px;"></i> 
                sistema bibliotecario
            </div>
            <div class="full-reset" style="background-color:#2B3D51; padding: 10px 0; color:#fff;">
                <figure>
                    <img src="assets/img/logo.png" alt="Biblioteca" class="img-responsive center-box" style="width:55%;">
                </figure>
                <p class="text-center" style="padding-top: 15px;">Sistema Bibliotecario</p>
            </div>
            <div class="full-reset nav-lateral-list-menu">
                <ul class="list-unstyled">
                    <li><a href="home.py"><i class="zmdi zmdi-home zmdi-hc-fw"></i>&nbsp;&nbsp; Inicio</a></li>
        
                    <li>
                        <div class="dropdown-menu-button"><i class="zmdi zmdi-account-add zmdi-hc-fw"></i>&nbsp;&nbsp; Registro de usuarios <i class="zmdi zmdi-chevron-down pull-right zmdi-hc-fw"></i></div>
                        <ul class="list-unstyled">
                            <li><a href="admin.py"><i class="zmdi zmdi-face zmdi-hc-fw"></i>&nbsp;&nbsp; Nuevo administrador</a></li>
                            <li><a href="usuarios.py"><i class="zmdi zmdi-accounts zmdi-hc-fw"></i>&nbsp;&nbsp; Nuevo Usuario</a></li>
                        </ul>
                    </li>
                    <li>
                        <div class="dropdown-menu-button"><i class="zmdi zmdi-assignment-o zmdi-hc-fw"></i>&nbsp;&nbsp; Libros y catalogo <i class="zmdi zmdi-chevron-down pull-right zmdi-hc-fw"></i></div>
                        <ul class="list-unstyled">
                            <li><a href="book.py"><i class="zmdi zmdi-book zmdi-hc-fw"></i>&nbsp;&nbsp; Nuevo libro</a></li>
                            <li><a href="catalog.py"><i class="zmdi zmdi-bookmark-outline zmdi-hc-fw"></i>&nbsp;&nbsp; Catalogo</a></li>
                        </ul>
                    </li>
                    <li>
                        <div class="dropdown-menu-button"><i class="zmdi zmdi-alarm zmdi-hc-fw"></i>&nbsp;&nbsp; Prestamos y reservaciones <i class="zmdi zmdi-chevron-down pull-right zmdi-hc-fw"></i></div>
                        <ul class="list-unstyled">
                            <li><a href="loan.py"><i class="zmdi zmdi-calendar zmdi-hc-fw"></i>&nbsp;&nbsp; Todos los prestamos</a></li>
                            <li>
                                <a href="loanpending.py"><i class="zmdi zmdi-time-restore zmdi-hc-fw"></i>&nbsp;&nbsp; Devoluciones pendientes <span class="label label-danger pull-right label-mhover">7</span></a>
                            </li>
                            <li>
                                <a href="loanreservation.py"><i class="zmdi zmdi-timer zmdi-hc-fw"></i>&nbsp;&nbsp; Reservaciones <span class="label label-danger pull-right label-mhover">7</span></a>
                            </li>
                        </ul>
                    </li>
                    <li><a href="report.py"><i class="zmdi zmdi-trending-up zmdi-hc-fw"></i>&nbsp;&nbsp; Reportes y estadisticas</a></li>
                    <li><a href="advancesettings.py"><i class="zmdi zmdi-wrench zmdi-hc-fw"></i>&nbsp;&nbsp; Configuraciones avanzadas</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="content-page-container full-reset custom-scroll-containers">
        <nav class="navbar-user-top full-reset">
            <ul class="list-unstyled full-reset">
                <figure>
                   <img src="assets/img/user01.png" alt="user-picture" class="img-responsive img-circle center-box">
                </figure>
                <li style="color:#fff; cursor:default;">
                    <span class="all-tittles">Admin Name</span>
                </li>
                <li  class="tooltips-general exit-system-button" data-href="index.py" data-placement="bottom" title="Salir del sistema">
                    <i class="zmdi zmdi-power"></i>
                </li>
                <li  class="tooltips-general search-book-button" data-href="searchbook.py" data-placement="bottom" title="Buscar libro">
                    <i class="zmdi zmdi-search"></i>
                </li>
                <li  class="tooltips-general btn-help" data-placement="bottom" title="Ayuda">
                    <i class="zmdi zmdi-help-outline zmdi-hc-fw"></i>
                </li>
                <li class="mobile-menu-button visible-xs" style="float: left !important;">
                    <i class="zmdi zmdi-menu"></i>
                </li>
            </ul>
        </nav>
        <div class="container">
            <div class="page-header">
              <h1 class="all-tittles">Sistema bibliotecario <small>Aniadir libro</small></h1>
            </div>
        </div>
        <div class="container-fluid"  style="margin: 50px 0;">
            <div class="row">
                <div class="col-xs-12 col-sm-4 col-md-3">
                    <img src="assets/img/flat-book.png" alt="pdf" class="img-responsive center-box" style="max-width: 110px;">
                </div>
                <div class="col-xs-12 col-sm-8 col-md-8 text-justify lead">
                    Bienvenido a la seccion para agregar nuevos libros a la biblioteca, deberas de llenar todos los campos para poder registrar el libro
                </div>
            </div>
        </div>
        <div class="container-fluid">
            <form autocomplete="off">
                <div class="container-flat-form">
                    <div class="title-flat-form title-flat-blue">Nuevo libro</div>
                    <div class="row">
                       <div class="col-xs-12 col-sm-8 col-sm-offset-2">
                            <legend><strong>Informacion basica</strong></legend><br>
                            
                            <div class="group-material">
                                <input type="text" name = "codigoCorrelativo"  class="tooltips-general material-control" placeholder="Escribe aqui el codigo correlativo del libro" pattern="[0-9]{1,20}" required="" maxlength="20" data-toggle="tooltip" data-placement="top" title="Escribe el codigo correlativo del libro, solamente numeros">
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Codigo correlativo</label>
                            </div>

                            <div class="group-material">
                                <input type="text" name = "categoria" class="tooltips-general material-control" placeholder="Escribe aqui el categoria del libro" required="" maxlength="70" data-toggle="tooltip" data-placement="top" title="Escribe el categoria del libro">
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Categoria</label>
                            </div>

                            <div class="group-material">
                                <input type="text" name = "titulo" class="tooltips-general material-control" placeholder="Escribe aqui el titulo o nombre del libro" required="" maxlength="70" data-toggle="tooltip" data-placement="top" title="Escribe el titulo o nombre del libro">
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Titulo</label>
                            </div>
                            <div class="group-material">
                                <input type="text" name = "autor" class="tooltips-general material-control" placeholder="Escribe aqui el autor del libro" required="" maxlength="70" data-toggle="tooltip" data-placement="top" title="Escribe el nombre del autor del libro">
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Autor</label>
                            </div>
                            <div class="group-material">
                                <input type="text" name = "pais" class="tooltips-general material-control" placeholder="Escribe aqui el pais del libro" required="" maxlength="50" data-toggle="tooltip" data-placement="top" title="Escribe el pais del libro">
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Pais</label>
                            </div>
                            <legend><strong>Otros datos</strong></legend><br>

                            <div class="group-material">
                                <input type="text" name = "editorial" class="material-control tooltips-general" placeholder="Escribe aqui la editorial del libro" required="" maxlength="70" data-toggle="tooltip" data-placement="top" title="Editorial del libro">
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Editorial</label>
                            </div>
                            <div class="group-material">
                                <input type="text" name = "edicion" class="material-control tooltips-general" placeholder="Escribe aqui la edicion del libro" required="" maxlength="50" data-toggle="tooltip" data-placement="top" title="Edicion del libro">
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Edicion</label>
                            </div>

                            <legend><strong>Estado fisico</strong></legend><br>

                            <div class="group-material">
                                <input type="text" name = "estado" class="material-control tooltips-general" placeholder="Escribe aqui el estado del libro" required="" maxlength="50" data-toggle="tooltip" data-placement="top" title="Estado del libro">
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Estado : Bueno, Regular o Malo</label>
                            </div>
                            <p class="text-center">
                                <button type="reset" class="btn btn-info" style="margin-right: 20px;"><i class="zmdi zmdi-roller"></i> &nbsp;&nbsp; Limpiar</button>
                                <button type="submit" class="btn btn-primary"><i class="zmdi zmdi-floppy"></i> &nbsp;&nbsp; Guardar</button>
                            </p>
                       </div>
                   </div>
                </div>
            </form>
        </div>
        <div class="modal fade" tabindex="-1" role="dialog" id="ModalHelp">
          <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title text-center all-tittles">ayuda del sistema</h4>
                </div>
                <div class="modal-body">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore dignissimos qui molestias ipsum officiis unde aliquid consequatur, accusamus delectus asperiores sunt. Quibusdam veniam ipsa accusamus error. Animi mollitia corporis iusto.
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="zmdi zmdi-thumb-up"></i> &nbsp; De acuerdo</button>
                </div>
            </div>
          </div>
        </div>
        <footer class="footer full-reset">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-xs-12 col-sm-6">
                        <h4 class="all-tittles">Acerca de</h4>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam quam dicta et, ipsum quo. Est saepe deserunt, adipisci eos id cum, ducimus rem, dolores enim laudantium eum repudiandae temporibus sapiente.
                        </p>
                    </div>
                    <div class="col-xs-12 col-sm-6">
                        <h4 class="all-tittles">Desarrollador</h4>
                        <ul class="list-unstyled">
                            <li><i class="zmdi zmdi-check zmdi-hc-fw"></i>&nbsp; Grupo BD <i class="zmdi zmdi-facebook zmdi-hc-fw footer-social"></i><i class="zmdi zmdi-twitter zmdi-hc-fw footer-social"></i></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="footer-copyright full-reset all-tittles"> 2017 Grupo BD </div>
        </footer>
    </div>
</body>
</html>
""")
