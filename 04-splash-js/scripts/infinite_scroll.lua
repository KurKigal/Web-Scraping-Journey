function main(splash, args)
  -- Sayfaya git
  assert(splash:go(args.url))
  
  -- Sayfanın yüklenmesini bekle
  assert(splash:wait(1.0))

  -- JavaScript ile sayfanın en altına kaydır
  splash:runjs("window.scrollTo(0, document.body.scrollHeight);")
  
  -- Kaydırma sonrası yeni verilerin yüklenmesi için bekle
  assert(splash:wait(2.0))

  -- HTML'i ve ekran görüntüsünü (debug için) döndür
  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
end