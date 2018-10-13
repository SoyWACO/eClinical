$(function() {
  $('#tabla').DataTable({
    "language": {
      "aria": {
        "sortAscending": ": activar para ordenar la columna ascendente",
        "sortDescending": ": activar para ordenar la columna descendente",
      },
      "paginate": {
        "first": "Primero",
        "last": "Último",
        "next": "Siguiente",
        "previous": "Anterior",
      },
      "emptyTable": "No hay datos disponibles en la tabla",
      "info": "Mostrando página _PAGE_ de _PAGES_",
      "infoEmpty": "No hay entradas para mostrar",
      "infoFiltered": "(filtrado de _MAX_ entradas totales)",
      "lengthMenu": 'Mostrar <select>'+
        '<option value="10">10</option>'+
        '<option value="20">20</option>'+
        '<option value="30">30</option>'+
        '<option value="40">40</option>'+
        '<option value="50">50</option>'+
        '<option value="-1">Todo</option>'+
        '</select> entradas',
      "loadingRecords": "Cargando...",
      "processing": "Procesando...",
      "search": "<i class='fa fa-search'></i>",
      "searchPlaceholder": "Buscar...",
      "zeroRecords": "No se encontraron registros coincidentes",
    }
  });
});