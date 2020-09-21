def imprime_dados_loja():
    # Implemente aqui
    nome_loja
    s01 = ("%s, %d %s" % (logradouro, numero, complemento))
    s02 = ("%s - %s - %s" % (bairro, municipio, estado))
    s03 = ("CEP:%s Tel %s" % (cep, telefone))
    observacao
    s04 = ("CNPJ: %s" % cnpj)
    s05 = ("IE: %s" % inscricao_estadual)
    stringResultado = "{}\n{}\n{}\n{}\n{}\n{}".format(nome_loja, s01, s02, s03, observacao, s04, s05)
    return print(stringResultado)
