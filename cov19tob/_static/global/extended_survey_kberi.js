const op_checker = (radio_id, op_id) => {
  let radio_tag = "#" + radio_id;
  let op_tag = "#" + op_id;
  let radio_parent = $(radio_tag).parent().parent().parent();

  const set_current_status = () => {
    if ($(radio_tag).is(":checked")) {
      $(op_tag).show();
    } else {
      $(op_tag).hide();
    }
  };

  set_current_status();
  radio_parent.change(function () {
    set_current_status();
  });
};

const show_after = (id, seconds) => {
  const tag = "#" + id;
  $(tag).delay(seconds * 1000).fadeIn();
};

const checkbox_hider = (checkbox_id, receiver_id) => {
  let checkbox_tag = "#" + checkbox_id;
  let receiver_tag = "#" + receiver_id;
  $(checkbox_tag).change(function () {
    console.log(checkbox_tag + " changed");

    if ($(checkbox_tag).is(":checked")) {
      $(receiver_tag).val(0).hide();
    } else {
      $(receiver_tag).show();
    }
  });
};

const checkbox_shower = (checkbox_id, receiver_id) => {
  let checkbox_tag = "#" + checkbox_id;
  let receiver_tag = "#" + receiver_id;
  $(checkbox_tag).change(function () {
    console.log(checkbox_tag + " changed");

    if ($(checkbox_tag).is(":checked")) {
      $(receiver_tag).show();
    } else {
      $(receiver_tag).hide();
    }
  });
};

const hide_others = (tag_list, num_choices_to_hide) => {
  $('input:radio').change(function (e) {
    // console.log("hide_others(): started");
    let selected_id = $(this).parent().parent().parent().attr('id'); // console.log("selected_id="+selected_id);

    let index_of_selected_id = tag_list.indexOf(selected_id); // console.log("index_of_selected_id="+index_of_selected_id);

    if (index_of_selected_id >= 0) {
      // console.log("loop entered:");
      for (let i = 0; i < num_choices_to_hide; i++) {
        // console.log("checking order "+i+"...");
        tag_list.forEach(function (tag, index, array) {
          if (is_unchecked_all(tag_list, i)) {
            $(radio_tag_maker(tag, i)).attr("disabled", false);
          } else {
            if ($(radio_tag_maker(tag, i)).is(":checked")) {
              $(radio_tag_maker(tag, i)).attr("disabled", false);
            } else {
              $(radio_tag_maker(tag, i)).attr("disabled", true);
            }
          }
        });
      }
    }
  });
};

const is_unchecked_all = (tag_list, i) => {
  // console.log("is_unchecked_all: i=",i);
  if (tag_list.every(function (item, index, array) {
    if ($(radio_tag_maker(item, i)).is(":checked")) {
      // console.log("false return");
      return false;
    } else {
      return true;
    }
  })) {
    // console.log("true return, and exit is_unchecked_all");
    return true;
  } else {
    // console.log("false return, and exit is_unchecked_all");
    return false;
  } // console.log("true return");


  return true;
};

const radio_tag_maker = (tag, i) => {
  return "#" + tag + "_" + i;
};