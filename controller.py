import view
import pbManager



def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                pbManager.open_file()
            case 2:
                pbManager.save_file()
            case 3:
                view.show_contacts(pbManager.get())
            case 4:
                # pbManager.add(view.new_contact_input())
                pb = view.new_contact_input()
                pbManager.add(pb)
            case 5:
                pb = pbManager.get()
                view.show_contacts(pb)
                index = view.input_id()
                contact = view.new_contact_input()
                pbManager.change_contact(index, contact)
            case 6:
                find = view.find_contact()
                result = pbManager.find(find)
                view.show_contacts(result)
            case 7:
                pb = pbManager.get()
                view.show_contacts(pb)
                index = view.input_id2()
                pbManager.delete_contact(index)
            case 8:
                print('Пока!')
                break