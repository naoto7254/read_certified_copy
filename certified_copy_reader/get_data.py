class DataGetter:
    def __init__(self, text_list):
        self.text_list = text_list
        
    def get_building_name(self):
        index_building_name = []
        for i in range(len(self.text_list)):
            if '建物の名称' in self.text_list[i]:
                index_building_name.append(i)

        # 【validation code】
        if len(index_building_name) == 0:
            print('建物名が見つかりません.土地の謄本とかで実行していませんか?')
            
        index_name_of_structure = []
        for i in range(len(self.text_list)):
            if '①構造' in self.text_list[i]:
                index_name_of_structure.append(i)
                
        if index_name_of_structure[0] - index_building_name[0] == 2:
            first_row_building_name = self.text_list[index_building_name[0]]
            l = first_row_building_name.split('│')
            result = l[1]
            
        else:
            # 建物の名称を全て取得し、文字列結合させ、'├'でsplitする
            data_str = ''
            for i in range(index_name_of_structure[0]-index_building_name[0]):
                l = self.text_list[index_building_name[0]+i].split('│')

                if l[0] == '┠':
                    break

                if l[0] != '├':
                    data_str += l[1]
                else:
                    data_str += l[0]

            data_list = data_str.split('├')
            result = data_list[len(data_list)-1]            
                
        return result