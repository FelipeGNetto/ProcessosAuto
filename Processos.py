import pyautogui as pg 
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from selenium.webdriver.chrome.options import Options

tela = Tk()

tela.title("Automação de Processos")
tela.geometry("792x537")
tela.resizable(False,False)

# imagem = ImageTk.PhotoImage(Image.open("E:\\Python_Udemy\\RPA\\gabarra.jpg"))
imagem = ImageTk.PhotoImage(Image.open("images\\gabarra.jpg"))
fundo = Label(image=imagem)
fundo.place(x=-2,y=0)

def tjsp():
    # Realizando a automação
    # nmr_proc = "00117749520220506" 1010191-42.2023.8.26.0597

    def tjsp_del():
        dig13.destroy()
        entryDig13.destroy()
        btn_voltar.destroy()
        dig4.destroy()
        entryDig4.destroy()
        nome.destroy()
        entryNome.destroy()
        botao.destroy()
        menu()

    def autoTJSP():
        nmr_proc1 = str(entryDig13.get())
        nmr_proc2 = str(entryDig4.get())
        name = str(entryNome.get())

        nav = wd.Chrome()
        nav.get("https://esaj.tjsp.jus.br/cpopg/open.do")

        pg.sleep(1)

        nav.find_element(By.ID, "numeroDigitoAnoUnificado").send_keys(nmr_proc1)

        pg.sleep(1)

        nav.find_element(By.ID, "foroNumeroUnificado").send_keys(nmr_proc2)

        pg.sleep(1)

        nav.find_element(By.ID, "botaoConsultarProcessos").send_keys(Keys.RETURN)

        pg.sleep(2)

        data = nav.find_elements(By.XPATH, '//*[@id="tabelaUltimasMovimentacoes"]/tr[1]/td[1]')[0].text
        msg = nav.find_elements(By.XPATH, '//*[@id="tabelaUltimasMovimentacoes"]/tr[1]/td[3]')
        
        message = f"Última atualização do processo: {data}\n Movimento:\n"

        for value in msg:
            message += f"{value.text}\n"

        pg.sleep(1)

        nav.close()
        
        result = messagebox.askyesno("Deseja enviar os dados pro cliente?", message)


        if result:
            zap = wd.Chrome()
            zap.get("https://web.whatsapp.com/")
            while len(zap.find_elements(By.ID, 'side')) < 1:
                pg.sleep(3)
            
            pg.sleep(2)

            zap.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(name)
            pg.sleep(2)
            pg.press("enter")
            pg.sleep(1)
            zap.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(
                message
            )
            pg.sleep(4)
            pg.press("enter")
            pg.sleep(5)

            zap.quit()

            messagebox.showinfo("Mensagem", "Dados enviados com sucesso")
        else:  
            messagebox.showinfo("Mensagem", "Envio de dados cancelado!")

    
    dig13 = Label(text="Número do processo: ", font=("Arial", 15), fg="white", bg="#1f1f1f")
    dig13.grid(row=1, column=0, padx=10, pady = 10, sticky="W")
    entryDig13 = Entry(font=("Arial", 15), width=20)
    entryDig13.grid(row=2, column=0, padx = 10)

    dig4 = Label(text="8.26", font=("Arial", 15), fg="black", bg="white")
    dig4.grid(row=2, column=1, padx=10, pady=10, stick="W")
    entryDig4 = Entry(font=("Arial", 15), width=5)
    entryDig4.grid(row=2, column=2, padx=10)

    nome = Label(text="Nome do cliente: ", font=("Arial", 15), fg="white", bg="#1f1f1f")
    nome.grid(row=3, column=0, padx=10, pady = 10, sticky="W")
    entryNome = Entry(font=("Arial", 15), width=20)
    entryNome.grid(row=4, column=0, padx = 10)

    botao = Button(tela, text="Pesquisar", command=autoTJSP, fg="#1f1f1f", width=10, font="Arial 10 bold", cursor="hand2")
    botao.grid(row=2, column=3, padx=5)

    btn_voltar = Button(tela, text="Voltar", command=tjsp_del, fg="#1f1f1f", width=10, font="Arial 10 bold", cursor="hand2")
    btn_voltar.grid(row=2, column=4, padx=5)

def trf3():
# 0005253-49.2015.4.03.6102
    def trf3_del():
                num_proc.destroy()
                entryNum.destroy()
                nome.destroy()
                entryNome.destroy()
                botao.destroy()
                btn_voltar.destroy()
                menu()

    def autoTRF3():
        try:
            nmr_proc = str(entryNum.get())
            name = str(entryNome.get())

            options = wd.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")

            nav = wd.Chrome(options=options)
            pg.sleep(2)
            nav.get("https://pje1g.trf3.jus.br/pje/ConsultaPublica/listView.seam")
            pg.sleep(2)
            nav.find_element(By.XPATH, '//*[@id="fPP:numProcesso-inputNumeroProcessoDecoration:numProcesso-inputNumeroProcesso"]').send_keys(nmr_proc)
            pg.sleep(2)
            pg.press("enter")
            pg.sleep(2)
            nav.find_element(By.XPATH, '//*[@id="fPP:processosTable:8346769:j_id226"]/a').send_keys(Keys.RETURN)
            pg.sleep(2)
            nav.switch_to.window(nav.window_handles[1])
            pg.sleep(2)
            msg = nav.find_element(By.XPATH, '//*[@id="j_id131:processoEvento:tb"]/tr[1]').text
            pg.sleep(2)
            nav.quit()

            result = messagebox.askyesno("Deseja enviar os dados pro cliente?", f"Última atualização do processo: {msg}")


            if result:
                zap = wd.Chrome()
                zap.get("https://web.whatsapp.com/")
                while len(zap.find_elements(By.ID, 'side')) < 1:
                    pg.sleep(3)
                
                pg.sleep(2)

                zap.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(name)
                pg.sleep(2)
                pg.press("enter")
                pg.sleep(1)
                zap.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(
                    msg
                )
                pg.sleep(4)
                pg.press("enter")
                pg.sleep(5)

                zap.quit()

                messagebox.showinfo("Mensagem", "Dados enviados com sucesso")
            else:  
                messagebox.showinfo("Mensagem", "Envio de dados cancelado!")
            

        except Exception as e:
            print(f"Erro durante a automação: {e}")



    num_proc = Label(text="Número do processo: ", font=("Arial", 15), fg="white", bg="#1f1f1f")
    num_proc.grid(row=1, column=0, padx=10, pady = 10, sticky="W")
    entryNum = Entry(font=("Arial", 15), width=25)
    entryNum.grid(row=2, column=0, padx = 10)

    nome = Label(text="Nome do cliente: ", font=("Arial", 15), fg="white", bg="#1f1f1f")
    nome.grid(row=3, column=0, padx=10, pady = 10, sticky="W")
    entryNome = Entry(font=("Arial", 15), width=25)
    entryNome.grid(row=4, column=0, padx = 10)

    botao = Button(tela, text="Pesquisar", command=autoTRF3, fg="#1f1f1f", width=15, font="Arial 10 bold", cursor="hand2")
    botao.grid(row=2, column=1, padx=5)

    btn_voltar = Button(tela, text="Voltar", command=trf3_del, fg="#1f1f1f", width=15, font="Arial 10 bold", cursor="hand2")
    btn_voltar.grid(row=2, column=2, padx=5)


def menu():
    def destruirTJSP():
        op.destroy()
        botao1.destroy()
        botao2.destroy()
        tjsp()

    def destruirTRF3():
        op.destroy()
        botao1.destroy()
        botao2.destroy()
        trf3()

    op = Label(text="Qual tipo de processo deseja pesquisar?", font=("Arial", 15), fg="white", bg="#1f1f1f")
    op.pack(pady=20)
    botao1 = Button(tela, text="TJSP", command=destruirTJSP, fg="#1f1f1f", font="Arial 10 bold", width=20, cursor="hand2")
    botao1.pack(pady=10)
    botao2 = Button(tela, text="TRF3", command=destruirTRF3, fg="#1f1f1f", font="Arial 10 bold", width=20, cursor="hand2")
    botao2.pack(pady=10)


menu()


tela.mainloop()