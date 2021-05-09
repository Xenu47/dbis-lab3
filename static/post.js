function try_update(event) {
  var table_row = event.target.parentElement.parentElement;
  var cells = table_row.children
  var form_name = cells[0].innerText
  var names = ['name', 'publisher', 'rating', 'genre']
  for (var i = 0; i < cells.length; i++){
    var temp = cells[i]
    var temp_text = temp.innerText
    if (temp.children.length != 0){
      break
    }
    else if (!isNaN(temp_text)){
      cells[i].innerHTML = '<input type="number" class="form-control" placeholder="'+temp.innerHTML+'"  value="'+temp.innerHTML+'" name="'+names[i]+'" min="0" max="5" step="0.1" required autocomplete="off" form="'+form_name+'">'
    }
    else if (temp.attributes.length != 0){
      if (cells[i].attributes[0].value == 'name'){
        cells[i].innerHTML = '<input type="text" class="form-control" placeholder="'+temp_text+'" value="'+temp_text+'" name="name:'+temp_text+'" required autocomplete="off" form="'+form_name+'">'
      }
      else if (cells[i].attributes[0].value == 'publisher'){
        cells[i].innerHTML = document.getElementById('publisher-select').innerHTML;
        var sel = cells[i].children[0]
        sel.options[sel.selectedIndex].value = temp_text;
        sel.options[sel.selectedIndex].textContent = temp_text;
        cells[i].children[0].setAttribute('form', form_name);
        cells[i].children[0].setAttribute('name', names[i]);
        cells[i].children[0].children[0].removeAttribute('disabled');
      }
      else if (cells[i].attributes[0].value == 'email'){
        cells[i].innerHTML = '<input type="email" class="form-control" placeholder="'+temp_text+'" value="'+temp_text+'" name="email" required autocomplete="off" form="'+form_name+'">'
      }
    }
    else{
      cells[i].innerHTML = '<input type="text" class="form-control" placeholder="'+temp_text+'" value="'+temp_text+'" name="'+names[i]+'" required autocomplete="off" form="'+form_name+'">'
    }
  }
  cells[cells.length-2].innerHTML = '<button type="submit" class="btn btn-primary" form="'+form_name+'">Update</button>';
  cells[cells.length-1].innerHTML = '<button type="button" class="btn btn-warning" onclick="cancel_update(event)">Cancel </button>';
}

function cancel_update(event) {
  var table_row = event.target.parentElement.parentElement;
  var cells = table_row.children
  for (var i = 0; i < cells.length; i++){
  	cells[i].innerHTML = cells[i].firstElementChild.getAttribute('placeholder')
  }
  cells[cells.length-2].innerHTML = '<button type="button" class="btn btn-primary" onclick="try_update(event)">Update</button>';
  cells[cells.length-1].innerHTML = '<a type="button" class="btn btn-danger" href="{{app_name}}/Delete/{{a.name}}">Delete</a>';
}
