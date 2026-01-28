function main(splash, args)
  -- 1. Sayfaya git
  assert(splash:go(args.url))
  
  -- 2. Sayfanın yüklenmesi için bekle (Argüman olarak gelmezse 0.5sn bekle)
  assert(splash:wait(args.wait or 0.5))

  -- 3. Sonuçları döndür
  return {
    html = splash:html(), -- Render edilmiş HTML
    png = splash:png(),   -- Sayfanın ekran görüntüsü (debug için harika)
    har = splash:har(),   -- Network isteklerinin listesi
  }
end