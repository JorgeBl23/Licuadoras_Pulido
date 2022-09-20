$(document).ready(function () {
    
    $('#carrito').DataTable({
        dom: 'Bfrtip',
        responsive: true,
        paging: true,
        autoWidth: true,
        buttons:[ 
			{
				extend:    'excelHtml5',
				text:      '<i class="fas fa-file-excel"> Exel</i> ',
				titleAttr: 'Exportar a Excel',
				className: 'btn btn-success'
			},
            {
				extend:    'print',
				text:      '<i class="fa fa-print"> Imprimir</i> ',
				titleAttr: 'Imprimir',
				className: 'btn btn-info'
                
			},
			{
				extend:    'pdfHtml5',
				text:      '<i class="fas fa-file-pdf"> PDF</i> ',
				titleAttr: 'Exportar a PDF',
				className: 'btn btn-danger',
            },
		],	

        "bDestroy": true,
        "language": {

            "lengthMenu": "Mostrar _MENU_ registros por página",
            "zeroRecords": "No se encontro registro",
            "info": "Mostrando página _PAGE_ de _PAGES_",
            "infoEmpty": "No hay registros disponibles",
            "search": "Buscar: ",
            "infoFiltered": "(filtrado de _MAX_ registros totales)",
            "paginate": {
                "next": "Siguiente",
                "previous": "Anterior"
            }
        }
    });
});