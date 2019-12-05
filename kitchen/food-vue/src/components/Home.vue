<template>
  <div>
    <mu-linear-progress style="position: fixed; z-index: 100" v-if="progress"></mu-linear-progress>
    <div>
      <template v-if="show.login">
        <Login @goMain="goMain" @openColorSnackbar="openColorSnackbar" @closeColorProgressbar="closeColorProgressbar"
               @openColorProgressbar="openColorProgressbar" @goRegistration="goRegistration"></Login>
      </template>

      <template v-else-if="show.register">
        <Registration @goMain="goMain" @openColorSnackbar="openColorSnackbar" @auth="auth"></Registration>
      </template>

      <template v-else>
        <div>
            <div>                           <!--left bar-->

              <mu-drawer width="256" :open.sync="open_drawer" style="transition: all .25s; background-color: #424242; z-index: 80">
                <br>
                <h1 style="text-align: center; color: #e0e0e0">Dashboard</h1>
                <br>
                <mu-list>

                  <mu-list-item button @click="" :ripple="false">
                    <mu-list-item-action>
                      <mu-icon value="dashboard" color="grey300"></mu-icon>
                    </mu-list-item-action>
                    <mu-list-item-title style="color: #e0e0e0">Order-stock</mu-list-item-title>
                  </mu-list-item>


                  <mu-list-item button @click="" :ripple="false">
                    <mu-list-item-action>
                      <mu-icon value="shopping_cart" color="grey300"></mu-icon>
                    </mu-list-item-action>
                    <mu-list-item-title style="color: #e0e0e0">Shops</mu-list-item-title>
                  </mu-list-item>


                  <mu-list-item button @click="" :ripple="false">
                    <mu-list-item-action>
                      <mu-icon value="tablet_android" color="grey300"></mu-icon>
                    </mu-list-item-action>
                    <mu-list-item-title style="color: #e0e0e0">Products</mu-list-item-title>
                  </mu-list-item>

                </mu-list>
                <mu-divider></mu-divider>
                <br>
                <br>

                <mu-list>
                  <mu-list-item button :ripple="false">
                    <mu-icon value="power_settings_new" color="grey300"></mu-icon>
                    <mu-list-item-title style="margin-left: 20px; color: #e0e0e0" @click='logout'>Exit
                    </mu-list-item-title>
                    <mu-list-item-action>
                    </mu-list-item-action>
                  </mu-list-item>
                </mu-list>
              </mu-drawer>
            </div>                           <!--left bar-->

            <div :class="[progress ? 'app-progress' : '', open_drawer ? 'draw-move': 'draw-return']">
              <mu-appbar style="width: 100%; text-align: right; position: fixed" color="primary">
                <mu-button icon slot="left" @click="open_drawer = !open_drawer">
                  <mu-icon value="menu"></mu-icon>
                </mu-button>
                <div :class="[open_drawer ? 'app-move': 'app-return']">
                  Genius Plaza
                </div>
              </mu-appbar>
Velit adipisci sollicitudin curae esse montes sint augue culpa ante. Arcu, minus, quam ducimus sunt iure! Aliqua minus! Congue tempus voluptate montes libero cumque placerat adipiscing proident, sequi. Sunt nibh lectus vitae aliquam purus adipiscing, maecenas? Malesuada consequuntur. Ullamco, aliquid. Arcu eros eros doloribus quis, suscipit incididunt fuga magnis quae, ullamcorper, fuga vero odit molestiae at minim! Laboris minus vitae exercitationem, leo, fugiat pharetra, repudiandae nam nesciunt aliquid, volutpat malesuada sollicitudin aliquip etiam, fuga optio, ex platea numquam? Mauris augue debitis nostrum laudantium distinctio, asperiores per sem ducimus itaque platea, magna rutrum? Debitis odio dui proident! Nostra officiis ipsa? Doloribus inventore, consequuntur. Occaecati do, similique sagittis eu cupiditate ornare tellus eu parturient! Semper aliquid dictum dapibus provident elit justo? Justo, ipsa illum fermentum quas penatibus inventore distinctio cillum quidem pretium? Sequi dolorum numquam error curabitur deserunt a doloribus. Nisi conubia sociosqu! Ullamcorper donec, dui! Conubia sapien doloremque elit dolorem quam ut faucibus iusto ante? Ultricies dignissim eu quo posuere quaerat illo! Suscipit aliquam vitae do varius! Eaque ullamcorper, temporibus, aliquid, hic nec et pretium scelerisque non repellat bibendum, laboriosam soluta nostrum gravida quibusdam quisque adipisicing mauris magnis ad dicta dolore eiusmod praesentium, omnis iusto torquent, vel, interdum debitis, malesuada rhoncus, veniam wisi culpa diam mauris, consequuntur pede. Quod molestie, dui. Tellus molestias. Congue suspendisse congue exercitation. Pariatur diam massa officia esse taciti.

Natoque ipsum modi ultricies facilisi quisque odio at senectus leo condimentum magnis quia? Odio quo, dignissim repellendus error! Tenetur tenetur? Nobis modi, placeat eveniet consequatur neque duis taciti sapien sagittis? Est illo autem hac reiciendis unde netus do provident quisque voluptatibus ligula tincidunt rem. Eius, malesuada volutpat tenetur? Magnam? Accusamus, elit dolores! Nobis vestibulum accumsan! Malesuada irure, cupidatat diam imperdiet. Maiores placerat cras! Quibusdam! Aliquam, blanditiis dui cumque litora asperiores, mattis potenti! Sem eu vestibulum, nihil similique distinctio cupiditate habitasse officiis tempore, impedit libero culpa ullam eligendi quos per accusantium, facilisis aliquid curabitur quisquam diam neque aliquip neque turpis delectus reprehenderit bibendum, ultricies faucibus praesentium, perferendis sociis mollitia magna sed ea quos, risus pellentesque, occaecat? Consectetur placerat at porttitor aptent nisl natoque error. Illum adipiscing fugit enim magnam dignissim sit culpa corrupti? Sagittis pulvinar justo! Laudantium arcu necessitatibus, vitae sapien? Illo facere taciti aspernatur. Enim fuga ut at, officiis vitae, aenean felis, voluptatibus facilisi, cursus tempora. Similique ligula lectus quasi sagittis! Nostrud incidunt cupiditate facilisi numquam pellentesque animi! Eveniet maiores. Facilisis eu interdum imperdiet habitasse, minim, asperiores varius occaecati impedit? Dignissim purus minima, ullamcorper quod quod, nostra ipsum wisi viverra? Rerum nascetur aspernatur iure odio feugiat? Accusantium tellus! Irure aptent lectus, fugit debitis aenean sapien imperdiet ipsum, dolore, velit blandit. Tenetur urna. Praesent blanditiis risus cupiditate! Nonummy fusce! Assumenda, assumenda vivamus montes.

Aliquam reiciendis taciti eaque eros error repudiandae hac beatae lorem soluta, orci optio purus, quas unde sint, quidem, architecto laoreet leo cupidatat quam reprehenderit! Debitis eiusmod habitant natus optio dolores illum curae doloremque! Illo, deleniti iusto amet cillum mollis maxime. Augue delectus, ad fugiat ratione? Non fames accusamus quam voluptates at esse, accusantium excepturi condimentum aliquam minima sagittis condimentum dicta, eget platea curae eveniet vel minim, imperdiet nemo tempus proin! Auctor quidem? Reprehenderit deserunt consequatur, aute proident ullam, assumenda quam, hac quo conubia nunc, explicabo! Eaque phasellus iaculis eligendi praesent nostrud ligula explicabo cupidatat unde facilisi. Harum consectetuer per rhoncus sit odit wisi sequi, sollicitudin? Eos quo magnam, quas condimentum magnam donec, aperiam libero, do auctor dolorum enim suspendisse harum, lorem ea similique curae harum tellus, cras ea, ultricies eius, donec rerum ridiculus habitant facere ullamcorper montes orci? Amet id saepe fames felis nisi, assumenda dolorem varius? Nascetur, neque ultrices, sed dolorem tortor consequatur torquent quia nec hac. Temporibus augue, dignissim omnis doloremque nemo? Quae augue quasi dictum. Nemo impedit ea mollit facere adipiscing eget voluptate, sunt metus lectus officiis varius vitae veritatis? Bibendum deserunt dolor at lectus minus luctus fames illo? Quod quae augue commodo. Platea animi eligendi nobis, soluta doloribus atque arcu tempor saepe veniam parturient, deserunt est! Doloremque, scelerisque aptent nisl, interdum numquam et a, libero volutpat, nostrum impedit.

Dignissimos ac habitant recusandae, tincidunt lacus viverra quae autem debitis nostra quam molestie eius sociosqu diamlorem? Mollit quibusdam fugit aliquid iste at ut fusce nam aut fringilla corrupti pretium montes, metus commodo? Penatibus primis animi commodo, convallis montes distinctio magnis, excepteur? Vestibulum ratione assumenda magna ullamcorper quos quis? Reprehenderit eos lacinia architecto! Vehicula culpa, culpa neque, cubilia! Iusto augue eligendi architecto scelerisque do delectus. Ornare. Voluptatibus. Velit magni, quas lacinia, molestiae elementum! Pretium quisquam soluta, porta, habitant, saepe? Quam nostrud? Deleniti porta nullam ligula! Aperiam assumenda rem felis, veritatis vel. Consequatur necessitatibus primis dui vero. Nibh iaculis distinctio, dui lacus? Metus illum, taciti culpa. Diamlorem ex? Pharetra ipsa! Voluptatibus ut, mi augue. Tempore nobis! Congue fames ipsum, pellentesque iaculis vulputate. Neque earum est ipsam eligendi, laboris! Lobortis ipsa dis nostra porttitor ipsum excepturi eu pede nobis sapien integer facilis consectetur, culpa beatae ducimus! Consectetur, sint accusamus, eum sociis? Ex sollicitudin luctus sociosqu quae libero tempus elit? Felis aperiam massa laboris ipsa mollis delectus tincidunt accumsan recusandae sapien porttitor! Varius libero curabitur consectetuer morbi, pulvinar! Curabitur nullam lobortis. Quo aptent aliquip! Similique voluptas, natoque, maxime, officia veniam scelerisque quasi minima potenti earum commodo porro cursus sunt? Eveniet incidunt? Aute dictum tempora, sem orci phasellus dolorem. Possimus similique proident torquent praesentium tellus, eleifend quibusdam, dolore viverra deleniti! Alias? Consequatur? Phasellus mauris totam ipsam, accusamus.

Doloremque dignissim. Quo lorem quibusdam arcu commodo id nec, fames ultricies, error, ultrices assumenda? Delectus saepe lacus do? Velit, auctor ultrices, placerat non reiciendis, cupidatat libero. Magnam in laborum? Excepturi, eiusmod tempus quidem! Duis, iure fermentum, accusamus litora suspendisse? Nibh sint lacinia rutrum faucibus pariatur. Repellat! Quae praesentium quisquam beatae asperiores proident tempora autem, dolorum deserunt placerat eos! Corporis incidunt rutrum massa quis deserunt, volutpat quam torquent voluptatem laudantium! Maxime condimentum aliquid donec rutrum? Magni, elementum donec dictum? Sequi hic? Eius, curae nam repellendus, porttitor, congue saepe hac debitis, exercitationem. Voluptates diam ad doloremque? Mollit primis, tellus! Iusto incididunt, assumenda aliquet veritatis blandit tempor pellentesque. Imperdiet quos rerum natoque velit posuere eu aliquip erat ultricies nisi penatibus, eligendi quidem massa. Sagittis, vestibulum, tristique deserunt, euismod! Dignissimos placerat inventore, ante imperdiet officiis nostrum? Condimentum elementum quod? Ridiculus, veritatis consectetur. Aliquid condimentum eveniet, cupiditate, lacinia mollitia, netus aenean dictum phasellus eros quo, totam nullam ultricies orci, fuga platea cubilia eaque cum vero parturient? Adipiscing blanditiis sunt quisquam sint adipiscing tenetur, malesuada exercitationem. Commodo hac in asperiores, orci ridiculus! Eget nisl semper! Justo, pharetra aliquet commodi voluptate odio viverra laborum arcu fringilla convallis, mollit aspernatur, aperiam cupiditate urna, sagittis, repellendus! Rutrum alias aliquid do alias magni ab tempora vehicula gravida, ornare irure venenatis! Gravida aliqua, aliquip magnam felis officia, sem beatae! Morbi aliquam molestie, quasi.

Corrupti potenti at nostrum praesent aptent esse sagittis massa hac lorem quas magna blandit ipsum saepe? Doloremque. Optio maecenas quis. Modi. Tellus, adipiscing dis, cillum congue. Ratione necessitatibus rem metus, ultrices fugiat ultrices minima ad? Fermentum, facilis quisquam nostrum minim taciti dolor, beatae voluptatum minus. Nibh ipsa corrupti, lobortis, purus! Anim consectetur ullam fringilla adipisicing porttitor, curae eius quaerat consequat, nunc augue autem mollitia vitae, venenatis! Potenti! Ab quas aliquam, faucibus molestias illo duis tincidunt imperdiet possimus primis aenean possimus. Commodo nulla, ornare dignissimos. Inventore minus justo sagittis? Tempora voluptatem praesent at justo pharetra accusamus aliquet, inventore tincidunt, reiciendis rutrum elementum asperiores, qui temporibus curae animi unde inceptos cumque elit expedita? Minima irure nostra totam parturient pede ullamco repellendus duis auctor nonummy provident laoreet? Platea, voluptates nesciunt proin iste dolorem debitis tempora, molestias platea cumque? Inventore leo labore, perferendis debitis, faucibus aut ligula delectus, corporis, a harum possimus accusantium! Labore accumsan recusandae mattis a, convallis in, risus! Dapibus? Hendrerit accusantium! Laudantium, habitant, diamlorem, eum lacinia! Odio lobortis ducimus vestibulum quo nulla? Penatibus fuga scelerisque! Mollitia exercitationem provident tristique aptent rem. Ullamco taciti vel, accusantium minim officiis convallis! Semper ullamco delectus? Diamlorem nec, donec interdum dis dolore libero veniam cras maiores? Bibendum, commodo! Sequi auctor, volutpat proident wisi deserunt sociis debitis, scelerisque vivamus natus! Vehicula ante, hac? Consectetuer, eligendi? Dis ducimus cum, pulvinar.

Vero, aute aliquid quisque ac pulvinar? Dolore consequuntur? Veritatis laboris inventore officia? Adipisicing aliqua! Natus molestie quod aliquam debitis quidem semper quod voluptates alias, penatibus dictum, proident? Vero senectus hac ac metus? Donec platea magnam rem! Dolorem, irure amet accumsan posuere quo, ullamcorper taciti euismod, ullamcorper, incididunt odio, fames aut mattis! Odio laboriosam per hymenaeos, saepe eu est consequat auctor! Numquam vitae. Repudiandae blanditiis ullamco? Tellus? Dapibus minim? Dapibus sodales, aute vehicula hymenaeos augue. Corporis congue excepteur augue? Anim consequuntur! Omnis, optio duis aspernatur? Blandit cillum incidunt ullam itaque volutpat commodi necessitatibus? Maiores inceptos dictumst posuere? Laborum felis, quas, magni voluptatum hendrerit ipsum ea, turpis! Inceptos mollis curabitur. Porttitor voluptate laboriosam iaculis facilisi porta vehicula modi anim quae voluptatem ultrices. Quam sequi quo metus inceptos parturient! Eiusmod iusto. Error amet nostrud inceptos ultricies! Lacinia dolorum habitasse deleniti auctor tempore veniam, sodales sit feugiat do? Ullamco? Sint nesciunt, eu, consequuntur nibh excepteur id convallis pulvinar, nobis placeat! Error sociosqu, quibusdam curabitur? Quam condimentum, dicta aptent dictum officia irure consectetuer dolore lacus primis phasellus luctus nemo, possimus dis consectetuer mollis nemo veritatis, aliquam semper rutrum pede ullam, tempus excepturi mollis dapibus felis sapien unde quam diam autem incididunt, augue venenatis elit corrupti! Ea eu ultricies nisi! Cillum lobortis. Venenatis? Hac phasellus leo, excepturi corporis ipsa mattis tenetur lectus, senectus, dicta accusantium corporis temporibus vivamus.

Perspiciatis commodo eveniet eu, eveniet, adipiscing wisi provident accusamus. Euismod rhoncus felis, voluptatem nec lobortis vestibulum mauris vel eum fugit ultrices unde aenean molestias, omnis sapien ullam? Laborum. Veniam sed natoque posuere accumsan integer aptent proin gravida purus nam iaculis, elementum ligula. Ornare temporibus vivamus orci tellus deserunt tincidunt auctor distinctio inventore iaculis litora? Sint litora, fames. Voluptatum quos eos? Diam nibh alias incidunt! Reprehenderit quibusdam, eos similique, malesuada erat viverra risus sed penatibus perspiciatis. Inceptos hac, ac, sem anim. Leo, facilisis debitis libero quae donec curae pellentesque consequatur hac, quidem! Optio lacus ea parturient duis hymenaeos rutrum aperiam, quia, ipsum, duis, irure bibendum gravida, dolore, pede modi, molestias numquam? Porta, urna ratione justo leo habitant, aliquam! Reiciendis cumque delectus risus adipisci ea adipisicing, placeat, quae eveniet a dolorum perspiciatis neque fringilla accumsan lorem adipiscing excepturi? Egestas commodi alias per. Voluptas nostrum anim eius, laboriosam facere! Aperiam porttitor? Dignissim ea? Pulvinar enim, lacinia laoreet distinctio odit fuga ante. Totam donec? Reiciendis class. Optio mauris quibusdam lectus iusto leo? Facilisis proin. Metus, ullam necessitatibus porta facilisi diamlorem conubia beatae integer viverra vestibulum natus urna dolores, pellentesque minim, itaque in veniam autem cupiditate quos, quasi phasellus nostrud, velit. Pretium mauris, tristique sem! Vivamus voluptatem adipiscing unde habitant magna distinctio iaculis. Maiores nunc inceptos ratione sodales ornare hac accumsan. Quasi incididunt qui, iure facilis laboriosam.

Earum risus tempore, sodales odio odit exercitation curabitur provident nec! Praesentium numquam tempore, diamlorem. Officia accusamus habitasse vero, labore exercitation quisquam numquam! Diam proin corporis, purus cupiditate imperdiet ligula senectus justo inceptos, mi nisl animi magni, totam eget nobis suspendisse est sem. Sapien aute mollit magna maiores ea, commodo habitasse litora sagittis. Convallis? Ultricies eos litora, architecto aperiam perferendis commodo adipiscing cillum! Saepe facilisi massa velit! Vivamus ornare proin? Modi, reprehenderit, qui, turpis penatibus debitis. Pariatur viverra aut euismod blanditiis, pretium ducimus diam lobortis tempore excepturi veniam praesent. Fames augue suspendisse commodo! Lacinia! Exercitationem eius dignissimos, placeat reprehenderit ante. Hymenaeos illum sociis! Pulvinar fames! Lacinia dolor odit ducimus. Volutpat maxime quisquam! Ultricies praesentium asperiores iure, neque imperdiet est posuere minima, dignissim ut architecto lacus dictum lacinia, mauris nullam diam cupidatat? Pharetra odit! Euismod fugiat nostra, deleniti necessitatibus, debitis! Mollit imperdiet aliqua ultricies leo pretium distinctio! Proident culpa primis suscipit minus omnis montes maxime ultrices sagittis modi vehicula nihil officiis ad, proident? Vestibulum nisi, nibh esse aspernatur maiores cum culpa corrupti! Purus? Eros tristique debitis cillum varius. Nemo pretium alias dolorum! Nunc ipsa quae maxime condimentum, molestiae, sociis, reiciendis bibendum veritatis rutrum quam. Commodo ut semper alias cursus aut! Nihil. Quis nesciunt nisi, magni ullam, tortor amet sapiente? Deserunt mauris phasellus? Commodi dolorem in exercitationem nobis metus! Cupidatat rhoncus morbi inventore, aut do.

Sapien laboriosam sit wisi nostra quo, quaerat repellendus irure torquent? Beatae praesentium eu eget. Pulvinar sodales animi volutpat volutpat architecto? Fames quidem, lacinia tempor. Maecenas occaecati nulla, interdum, magnis eum id exercitationem inventore ligula porttitor aut dolor aspernatur inventore viverra! Condimentum semper suscipit tincidunt. Habitasse tellus magna fames error, ullamcorper, amet litora wisi aliqua nemo modi, proident fames donec autem! Odit quas pulvinar, in, dignissimos, luctus similique quia, inceptos cupiditate dolorem bibendum, explicabo omnis itaque, ridiculus, sociis aliquip? Sollicitudin non! Accumsan purus conubia montes, libero, sint, blanditiis doloremque, commodo eiusmod! Conubia imperdiet platea optio habitant amet sit dolorem laborum magna reprehenderit cubilia ex enim magna? Minima culpa cupiditate odio molestiae tenetur veniam, molestie condimentum elementum minus! Dolor nascetur parturient maxime! Iure sit tempus, tempore aliquet tempora, assumenda est? Primis libero, atque dolore beatae ridiculus minima officia odit officia. Eu montes? Metus dolor eiusmod quo? Iure. Deleniti adipisicing? Interdum malesuada cumque eiusmod tristique expedita dictum mi aperiam, molestiae? Porro minima erat? Molestie platea eius eu dolores? Fermentum quam dignissim, facilis. Temporibus, iaculis, quasi, blandit luctus potenti congue. Etiam vulputate integer pretium. Risus facilisi! Dapibus odit. Cum quo, iusto tincidunt montes culpa, elementum do, quisquam quisquam illo mollis erat dolore exercitationem consequatur et exercitationem non. Eligendi! Cras laoreet cras quidem massa cupidatat. Earum proin gravida beatae quae nesciunt! Sapien, eros curae mattis, placeat quam.

Mauris urna? Egestas mollis ipsa sem quasi dolor, minim corporis placerat provident occaecati facere ab bibendum aute cursus adipiscing ipsam dictumst? Fermentum sequi natoque, porro aenean fugiat eu, perspiciatis pulvinar incididunt voluptatibus excepteur proin optio vehicula luctus blandit nostra ducimus, deleniti dictumst aptent! Lacus, quod? Nonummy proident rhoncus? Distinctio, libero? Quidem error fugit? Vitae porttitor elit. Aliquip accumsan placeat ultricies? A ipsam. Recusandae iusto, eaque consequatur incididunt a nulla officiis corporis sequi, neque aperiam tristique, nostrum. Maecenas euismod ea cupidatat, numquam totam culpa nam mollitia impedit ex nostrum, repellendus, senectus, voluptates. Augue posuere molestie possimus sapien, egestas diam! Aliquet vivamus! Ducimus quo cum parturient per habitant, illo sequi? Odit reprehenderit! Delectus! Cum! Quisque perspiciatis quo morbi sapiente rutrum rerum commodo. Do nostrum fringilla, nam nunc veniam, architecto cubilia? Laborum? Netus, conubia dicta. Venenatis laborum, quisquam quidem vitae orci. Et placeat, eum, fugiat minus aspernatur cillum. Dis montes tincidunt ipsum do! Ullamcorper non aptent voluptas, phasellus eius sunt facilisis, id qui, nihil voluptate primis quos dolore metus? Aliquam mollis! Malesuada suspendisse exercitation morbi, enim in mus, exercitation, inceptos dolorem dolorum amet rem molestiae. Qui sociis! Enim corporis dignissim hymenaeos risus. Voluptatibus irure condimentum, sed similique faucibus habitasse. Facilis, quis, veniam distinctio, quod quibusdam sagittis quam erat? Ex placeat aptent, neque fuga ligula! Nunc aliquam pulvinar ea? Porttitor odio cillum nisi adipiscing! Cras repellat.

Convallis mi sunt integer officiis, proident! Molestie! Condimentum phasellus irure, quae? Minima? Cupidatat repudiandae asperiores! Ultricies nulla dis, laboris, culpa, distinctio habitant volutpat massa porttitor est maiores, cubilia, rerum maxime, ipsum taciti donec nascetur architecto, turpis ratione magni, sociosqu dolorum, netus itaque? Incididunt ipsa inventore qui nesciunt conubia? Repellat distinctio, nullam modi dolorum nulla perspiciatis facere. Faucibus eleifend! Praesent aliquid elit condimentum sem. Aptent diamlorem aliquip pretium rem! Perspiciatis risus deserunt dolor eos nobis cumque sint deserunt? Leo, labore pariatur atque venenatis! Adipisci proident, vulputate, quia, in metus, irure penatibus? Illum proin? Blandit harum ipsum? Autem iaculis rhoncus. Exercitationem convallis! Felis dolore. Quia quibusdam fames elementum aut facilisi, pulvinar fermentum! Dignissim non impedit dolores, laboris? Accusantium. Vitae odit mi, ut, architecto eu sodales elit animi harum provident quaerat integer! Expedita lacinia officia purus quia unde. Ex velit auctor sociis similique vehicula, rhoncus recusandae, auctor, excepturi elementum? Penatibus non pulvinar facere! Sint facilisis leo semper natoque eveniet! Exercitation cubilia commodi venenatis accusamus aliquet, vulputate temporibus suscipit, tristique eget iaculis, nulla quasi! Error mollis quis, repudiandae penatibus accumsan, numquam nihil bibendum, tellus? Lacinia aperiam massa magnis inventore risus ad penatibus nostrum itaque, dolore blandit. Repellendus cumque voluptas, quibusdam, assumenda cumque! Aenean rem unde blandit magna? Parturient, sagittis sunt taciti dolores! Tempus incididunt eiusmod irure do arcu blanditiis, facilisis, deleniti duis fringilla sociosqu. Voluptatum eu.

Aliquid corrupti veniam. Apeiditate in, quaerat nibh elit nisl, litora excepturi pellentesque, accusantium adipisicing cumque laoreet nesciunt pellentesque reiciendis. Sequi class! Assumenda. Sem repellendus diamlorem ultricies cras! Veritatis rem expedita voluptatum montes eos. Officia natoque class eveniet. Mi molestie, assumenda laoreet veniam platea convallis occaecati atque ornare, sociis, repellendus tellus ipsam euismod auctor. Metus hac aut maxime sunt eius pulvinar, odio, dignissim soluta tristique dolor eligendi! Odit nonummy rhoncus! Dictum gravida nostrud asperiores recusandae vitae integer cupiditate arcu, augue luctus nulla imperdiet cupidatat? Hac adipisicing consequuntur delectus repellendus vero quam magnam curae hic, iaculis facilisi enim metus! Rerum, nostrud? Vel beatae sollicitudin aliqua dapibus, voluptatum hac rhoncus ullam? Suscipit pulvinar vivamus nostra dolores massa harum, tellus luctus viverra a. Natus fames atque exercitationem dignissimos fames orci, nibh platea porro consectetuer voluptate? Deserunt suspendisse, feugiat placeat nascetur deserunt! Vitae reiciendis mauris. Autem, congue sociosqu ratione sit feugiat elementum? Ridiculus. Lacus porta atque, deserunt, pretium. Libero, hic dolorum iusto nam, delectus, laoreet turpis, suscipit? Consequatur! Volutpat ridiculus, felis. Accusamus. Hic delectus magni nulla parturient id! Necessitatibus lacus, congue sapien! Elit aliquet, ad mollitia eum? Doloribus, aliquid? Commodi, molestias nascetur, aliquip, consectetuer cubilia praesentium egestas, quasi, corporis per minima architecto, minim, tortor harum ea? Egestas! Ultricies fames. Tristique at per impedit ab facilisi etiam tortor voluptates. Montes! Beatae eius nonummy facere nostrud.

A praesent netus sollicitudin imperdiet cursus, parturient facere lobortis exercitationem, semper accumsan wisi totam sapien, montes, nibh, at felis atque. Dignissimos sunt lectus! Aliquam, blanditiis. Impedit ea! Taciti, qui litora rerum convallis soluta curae ex exercitation sequi architecto incidunt ut quo feugiat hymenaeos etiam vivamus. Accumsan ipsum cubilia? Ab cubilia dapibus nascetur quaerat iste, curabitur quae, hymenaeos, dignissim wisi? Purus pharetra doloribus architecto minus accusantium eveniet iure minus? Eleifend voluptas, laborum sequi, senectus, quo blandit reiciendis vivamus habitasse. Quisque vulputate vero quo ullam consequat hac, tincidunt autem delectus veritatis reiciendis. Assumenda tellus voluptatem posuere, parturient netus, labore corporis quasi, excepturi quisquam excepteur! Soluta mattis. Blandit. Laoreet ex quam curae deserunt voluptates nostrud minus orci corrupti eleifend tellus diam illum, possimus? Accusantium maxime consequuntur posuere fuga autem, parturient elementum totam inceptos platea quod, accusamus, varius magnis, eos magni vero! Dolore ultrices vestibulum mauris litora. Primis! Ab explicabo maxime potenti pariatur possimus, curabitur molestiae incidunt urna! Praesentium nam, blandit amet suscipit etiam cupidatat assumenda felis per per, bibendum vivamus, cupiditate! Praesent, molestias tempus wisi habitant esse, eveniet auctor saepe quaerat hic voluptate! Curae cumque enim tenetur repudiandae? Penatibus suspendisse reiciendis taciti! Eaque, dignissimos magnam! Reprehenderit dolorum incididunt netus maxime magnis, quae suscipit, parturient sit natus diamlorem, laborum placerat voluptate erat adipiscing? Adipisicing, consequat eros quaerat veniam quos? Reprehenderit voluptate eget veritatis tempora? Officia sapiente.

Doloremque tempor? Pariatur? Quos reiciendis nullam! Sodales lectus tempor congue cras adipisicing cum ipsum. Fusce! Conubia dictumst itaque? Ea pede malesuada sociis consectetuer aspernatur! Rerum possimus, labore fugiat, sociis ultricies, modi aut anim torquent quas do? Corrupti turpis, doloribus feugiat bibendum odit nibh, phasellus rhoncus sem? Risus sed elit aspernatur, laboriosam, aptent, wisi nesciunt exercitationem irure labore tempor, repudiandae aspernatur aliquam. Dis etiam, iaculis do fuga, aliquam rhoncus, necessitatibus expedita ipsum, convallis, provident potenti! Duis nostra. Porta iusto diamlorem corporis ad. Sociis, sed, nostrum? Feugiat iusto cillum class nunc ullamco eaque. Tellus quia blanditiis donec enim! Veniam ullamco et irure quisque facilis, sociosqu aut nostrud perspiciatis consequuntur esse id morbi culpa. Vulputate? Adipisicing cupidatat, convallis nascetur orci. Eveniet, maiores aenean perferendis aliquam facilisis! Aut, quo excepturi, suscipit dicta, accusamus sem platea penatibus? Dolorem quaerat repudiandae proin exercitationem tellus. Consequat minim quidem pede vero platea? Mollit hac quos itaque phasellus facilisi pulvinar curabitur! Consectetuer, arcu reiciendis incidunt potenti, saepe viverra viverra, per molestiae. Assumenda malesuada ullamco suscipit iste maiores, doloribus? Etiam, erat sapiente purus imperdiet! Porta dicta? Corrupti? Accumsan risus ullam, donec justo dapibus qui officia itaque autem, donec vel mauris exercitation rem consequuntur rem proin, commodo maecenas magnam, imperdiet inceptos, dis vel ratione dapibus quasi adipiscing. Natoque curae! Aliquid, turpis. Consectetur nascetur, atque tortor quae mauris vivamus dolorum. Laoreet consequuntur, quis cupidatat.

Tenetur natus optio dolore dolore labore curabiur viverra consequat interdum. Quidem, sagittis ab eligendi ipsa autem! Sociosqu ullam, aliquet taciti, laboris autem ornare quaerat! Sociis quos officia cum natoque ullam officiis fermentum? Officia! Facilisis class suscipit iste inventore ad facilis, ante ipsam, augue officia, tortor repellendus voluptatem duis, porta irure, soluta error metus! Diamlorem, pellentesque purus. Sagittis laudantium veritatis a? Ullam accusantium eveniet voluptate officia! Semper? Vitae erat minima montes adipisci morbi, perferendis eaque distinctio, cum alias ridiculus corrupti praesentium nascetur, nobis possimus itaque! Recusandae non maiores tortor duis itaque. Dignissim, cumque tellus minima per nostra, nam aliquam euismod ullam sociosqu tempora ipsum egestas fugiat. Ipsum maxime a, vitae hac anim autem, expedita. Curae. Quas lobortis nostrum! Accumsan platea at rem debitis platea, non? Voluptas sit id hic, a anim? Similique nisi interdum, litora voluptatum minima bibendum, iaculis aspernatur aperiam magnam consequuntur, purus proident gravida sapien ullamcorper quae ultrices ornare egestas tincidunt ullam doloremque ipsa senectus quibusdam maxime alias! Nonummy. Nostrum consequat? Nullam asperiores commodo fermentum torquent quos! Eu! Curabitur dignissim a platea in metus? Justo, at eos purus sem. Occaecat sollicitudin! Nobis magnis donec, risus natus sed morbi. Veritatis. Nonummy provident placerat pariatur quisque cillum ullam odit necessitatibus amet repellat illum, vivamus molestie corrupti hac molestiae reiciendis quo porta, laudantium nec, praesentium dolorem tempus mus, provident provident dapibus magni! Curabitur malesuada.

Officiis feugiat beatae mus fuga. Iure! Nec quaerat mi impedit leo a, praesent nisl veritatis tellus ornare, facere? Pariatur dolorem orci cupidatat? Sapiente molestie cubilia diam sapien tempus! Ab necessitatibus! Lacinia class dapibus eos, morbi repellat et incidunt molestiae! Aliquet! Facilis error reiciendis earum distinctio, magnis facere magnam aliquam dolorum? Quisque incididunt? Non molestias mollit placeat, proident morbi etiam natoque! Maiores sapiente taciti commodi veniam fermentum, unde cras? Placerat eu, vestibulum volutpat, dolor accusamus erat viverra quam phasellus quasi! Incididunt, dolor tellus pretium repellendus, consequat suspendisse aute pretium wisi voluptas, lacus quo, hic maecenas, soluta interdum, eligendi aliqua tempor, elementum. Facilis, iste commodo libero minima! Cras rerum aperiam sapien laboris! Platea pede nibh eius conubia potenti, vehicula ex aenean, alias, nesciunt rhoncus ullamco omnis, hendrerit! Consequuntur. Vitae iure? Architecto, deserunt proident ultrices vulputate possimus. Voluptatem orci? Maecenas aliquet facilisis molestias mollitia purus cillum erat, ea platea nisi aliquam do dolorem quibusdam consequat! Mattis, cupiditate! Accumsan, aspernatur, minima facilis diamlorem iure curae amet placerat iste occaecat lacus laborum maxime? Hymenaeos! Integer platea sagittis eveniet dui, fames sed ligula eum aperiam similique, eos porta blandit eos? Maiores ipsa! Luctus ducimus unde, enim potenti facilisis, ducimus assumenda eos! Euismod purus optio quis facilisis nascetur do metus eiusmod, metus rutrum est repellat, curae omnis. Saepe quas culpa provident nascetur excepturi primis suspendisse lectus deleniti, nullam maxime.

Massa sem vehicula sociis voluptatem eligendi, posuere veniam dolorum urna platea? Labore nisl, arcu elementum, curae parturient consequatur, per inventore, commodo quidem, molestias itaque. Minima odit tenetur ducimus at dignissim, dui hymenaeos pede, aenean ante, maxime minima morbi quia quisque, ipsam donec, sem ipsam quo mollis! Eius imperdiet, praesent sollicitudin harum? Voluptatem? Qui tempora! Elit harum? Vel mattis sapien a! Tempor volutpat elementum cupiditate qui quidem. Reiciendis odio itaque dolores mauris ullam! Labore, porro egestas aptent leo pretium, magna debitis, pharetra lorem enim porro nisi laboris iure ornare, eaque cupidatat potenti aptent distinctio nisl aliquet ullam corrupti senectus deserunt! Ridiculus explicabo deserunt, atque explicabo? Libero, doloribus reiciendis maxime facilis sit porttitor facilis quasi eget, netus corrupti nibh nam facilisis auctor per error adipiscing ducimus, mollitia perferendis, lacinia praesentium urna pellentesque maxime rutrum etiam sapien. Deserunt diam lacus dicta? Morbi eveniet, ab, cras felis senectus, ac! Beatae! Donec lobortis sint! Consectetur? Quia dolorum elit eaque! Neque voluptatem rem dicta ullamcorper cubilia quibusdam senectus eu distinctio tincidunt blanditiis! Vitae qui? In dicta, eaque maxime pariatur fusce fermentum tristique non? Feugiat ullamco diamlorem, per autem, incidunt nesciunt nostra! Aliquid, aliquip, rutrum, odio! Quo vero urna unde mollis in eius, habitasse consectetur? Proident culpa, ut est auctor rutrum perspiciatis repellendus suscipit, occaecat sit eveniet, veniam pharetra. Risus irure tincidunt urna turpis sollicitudin ipsum nam quae! Mauris.

Voluptatibus amet, cras incididunt! Porta vivamus? Velit varius purus, veritatis torquent recusandae lobortis quidem, rem adipisicing hendrerit ipsam, nec nostra maecenas quis fermentum lobortis? Ex lorem tortor. Luctus? Quas ligula? Arcu aenean pulvinar hic nostrum mus cursus illo autem ab, cillum rem. Platea officiis, harum atque, ea quae, torquent tenetur ridiculus sint primis? Voluptatum anim tempor sed odio maxime nibh. Possimus nascetur! Class consectetuer, dolores ab, tellus duis quo fugit, saepe labore vulputate cursus fusce. Rutrum tempora fringilla enim voluptatum! Congue fuga necessitatibus? Cumque repellat viverra, quidem nobis? Pulvinar asperiores asperiores, voluptas mollit? Platea rutrum pariatur qui massa consectetuer cupidatat tempus vel natus incididunt, suscipit ad mollitia explicabo convallis elementum! Quia, pharetra! Curae ipsa, maiores do enim phasellus atque fusce, laoreet malesuada dicta eleifend molestie, ipsum. Molestias deleniti vestibulum maecenas. Mi taciti cumque, tempus phasellus parturient! Laboriosam aliquip! Eaque fuga, exercitationem deserunt ridiculus? Massa laboris eget convallis fringilla totam nemo! Inceptos cras consectetuer voluptas diam curae, ultricies proident aute duis quia aliquip incidunt quo penatibus. Ab porro asperiores, cum dignissim? Dolore aenean? Nonummy reiciendis, nunc pede omnis repudiandae magnis aute sem tristique gravida neque consectetuer nulla, curae odit, faucibus doloremque et porttitor, nostra maxime aliqua ipsam, fugit magnis conubia dui aliquip accusantium diam omnis corrupti sociosqu rutrum diamlorem, necessitatibus nisl! Aliquet integer fusce auctor voluptate at. Nostrum minus vehicula tempor! Placerat pretium.

Provident primis perspiciatis dolor, eu exercitationem, nostrud voluptatibus sit explicabo vero aspernatur? Eos expedita eros quos, laboriosam habitant posuere, quaerat? Varius. Auctor, nostrud optio? Porta. Occaecati faucibus euismod, interdum aenean ea ex impedit augue impedit, vel? Id reprehenderit consectetur assumenda, taciti placeat ultricies donec morbi, quidem nesciunt, nostrud voluptatibus beatae? Ultrices ipsa sapiente, ullamco animi id, eu habitant voluptatem, diamlorem? Blanditiis eiusmod magni sint. Id sed a omnis fugiat vehicula blanditiis rem occaecat magni soluta laboris quas! Aperiam, porttitor vehicula. Eu ullamcorper, aliquam earum pulvinar viverra erat conubia repellat assumenda! Quo lobortis porro iusto eveniet placerat, pulvinar habitasse deserunt nostrud? Commodo sunt quam euismod, aptent ultricies praesentium facere tempor doloremque ea sequi parturient commodi fuga totam mollitia? Minim vehicula sodales taciti nisl? Arcu metus asperiores eos lectus odit placerat hendrerit hendrerit auctor? Vitae laudantium varius voluptates? Dis dolorem, explicabo faucibus nobis deleniti. Dicta? Mattis? Cubilia ad sociis blandit, natoque maxime condimentum tempor pellentesque officiis, eros irure labore, qui necessitatibus scelerisque eligendi eaque dolore nesciunt rem ea minima ullamco mollit mus mollit, congue duis facere laborum perferendis! Facilisi omnis ornare dolor sunt auctor ipsam totam, suscipit necessitatibus, ultrices quidem laoreet, parturient aspernatur molestiae. Voluptates optio labore, voluptates error soluta, quaerat tempus mi hendrerit venenatis, aspernatur ornare ducimus urna, laborum, vivamus tincidunt, egestas potenti velit! Augue eros, ut quis perspiciatis diamlorem! Primis proin, voluptatum.

Nesciunt condimentum ullamcorper, hac, aliquet sint? Viverra luctus optio primis sodales sunt, pulvinar maecenas magnis! Hic pede similique quisquam tortor iusto feugiat quas platea provident adipisicing nec suscipit facilisis nibh. Nullam, nonummy, pariatur at do parturient accumsan, in lacinia cras, dis culpa labore senectus? Metus exercitationem? Ante nibh dapibus semper, ut tempore sapiente dolores ut massa odit erat adipiscing perferendis donec etiam, suscipit? Deserunt varius scelerisque? Veniam doloremque, recusandae parturient corrupti modi! Esse tempus tempus proident feugiat luctus ullamcorper deleniti. Alias cumque eius hymenaeos? Pulvinar? Irure nonummy. Morbi porttitor sapien pariatur at. Harum accusantium fames numquam? Gravida magnam, cras sapiente, aperiam purus porta est, sagittis malesuada, ut quas. Corrupti sollicitudin. Nam cum quibusdam repellat, nostrud ullamco assumenda orci bibendum integer. Iste sapien volutpat nec integer, provident fuga nibh adipiscing earum laudantium cupidatat tincidunt, recusandae ullamcorper eveniet ullamcorper aliqua quidem facilisi. Accusamus deserunt irure quos, quos. Rhoncus maxime risus, fugit laboriosam. Nobis iste, odit leo tristique integer dicta orci consectetur leo suspendisse habitant. Luctus hic, fusce sagittis sociis hymenaeos amet interdum ratione nisl, aliquid nulla amet commodo. Tempor scelerisque, ducimus donec dignissim velit habitant natoque iste auctor iusto praesent animi nisl debitis, eleifend, rutrum asperiores possimus, molestiae! Taciti ante? Hymenaeos cupidatat do exercitation! Ducimus reprehenderit ornare ab eum voluptatem, sed excepturi, error officia error ea aliquet curae ac cillum convallis commodi, nobis maiores.

Id hic tempus mauris debitis, sit, quidem, quis ipsam, ante consectetuer, aliquid! Potenti incidunt. Magni quis feugiat rhoncus nostrud sapien sint quod aliquet officia! Commodi habitasse voluptates phasellus risus! Venenatis. Gravida praesent sodales quidem molestie vitae! Omnis quasi potenti assumenda, illum adipisci rerum. Reiciendis, libero. Facere, doloribus imperdiet netus luctus. Qui ipsa ridiculus dignissim, dolor sociosqu sint fusce? Mollis odio, cupidatat hendrerit exercitation, minus. Fuga iste adipiscing inceptos, scelerisque et exercitation possimus elit, malesuada mollitia nam leo minus torquent tristique a accusantium? Cras hic? Mattis doloribus ad, porttitor porttitor mollit? Perspiciatis nec luctus luctus voluptatum, netus optio quidem conubia? Neque taciti blanditiis litora, proident? Tortor nascetur error alias. Mollit vehicula, elit doloremque? Irure proin nisl numquam nullam eu vestibulum id faucibus hac conubia, ex nec ultricies sociosqu anim montes rutrum, lobortis eveniet ligula feugiat eos? Ullam euismod in, dolore viverra eget arcu tortor nisi, aspernatur placerat do luctus nostrum adipisci justo sint mollitia? Urna mollitia ligula, cras cursus rhoncus felis minus consequat! Tempus mollis, suscipit. Molestie adipisicing ipsam magnis et! Assumenda, eos, metus amet quaerat, consequuntur? Eveniet. Massa consectetur ipsa, diamlorem congue curabitur rem sociosqu dolorem asperiores autem nam, venenatis, praesentium vitae aliquid sint urna? Anim? Adipisicing minima expedita quaerat congue rhoncus voluptates magnis atque corporis facere ridiculus quos fringilla ridiculus provident viverra occaecat fringilla, quis. Mattis quis eaque. Laborum! Ab! Luctus.

Fermentum quisquam felis erat vestibulum cursus, cubilia, aptent volutpat wisi turpis sociis. Vel phasellus eveniet, minim, tristique habitasse dignissim viverra exercitationem exercitationem ipsa fringilla scelerisque corporis atque? Taciti. Fames tristique, eveniet fugiat porta, mollitia provident. Quisque, nibh faucibus soluta faucibus? Habitasse commodi curae nunc perferendis totam urna sapiente? Tincidunt eu, itaque numquam dolor minima nostrud possimus consequuntur accusamus accusamus pharetra et orci torquent tellus quisquam, consequat sagittis consequat tincidunt alias iusto voluptas, diam rem cupidatat maxime hac minim elementum a orci, neque metus risus, cillum cupiditate odit nihil commodo pariatur, eiusmod sit quisque similique cupiditate tellus etiam ac odit suspendisse maiores parturient natoque feugiat! Dignissimos impedit, odit inventore, porro sit? Vel, rerum! Necessitatibus quibusdam error? Sint nulla curae. Iusto mollit. Enim quibusdam commodo in maxime tellus risus quo varius ligula torquent magnis sed vestibulum adipisicing? Class dignissim ullam voluptatum cumque vivamus aperiam, voluptas dapibus? Inceptos quod eiusmod vel vero lorem? Inceptos quisquam dapibus! Dui enim excepteur varius, aptent culpa justo, ea, illo. Suspendisse urna sunt pulvinar sapien interdum placeat nonummy tempus veritatis litora illo nobis eum sociis mauris erat fames? Fugit enim, orci odio ipsum semper morbi accumsan porro pariatur, incidunt ipsam eaque corrupti mollitia cupidatat excepteur sollicitudin voluptatem luctus. Voluptas ab penatibus consequuntur, eius debitis netus? Tenetur tristique! Hac culpa felis placeat sapiente orci consequatur. Vitae pellentesque voluptatem etiam, porro, do.
            </div>
        </div>
      </template>
      <mu-container>
        <!--          <OrderList v-if="show.order_list" @openColorSnackbar="openColorSnackbar" @goOrder="goOrder"></OrderList>-->
        <!--          <Shops v-if="show.shops" @openColorSnackbar="openColorSnackbar"></Shops>-->
        <!--          <Products v-if="show.products" @openColorSnackbar="openColorSnackbar"></Products>-->
        <!--          <Order v-if="show.order" :order_num="order_num"></Order>-->
      </mu-container>


      <mu-snackbar position='top' color="success" :open.sync="snackbar">
        <mu-icon left value="info"></mu-icon>
        {{ snackbar_message }}
        <mu-button flat slot="action" color="#fff" @click="snackbar = false">Close</mu-button>
      </mu-snackbar>
    </div>
  </div>
</template>

<script>
  import Login from "./Login";
  import Registration from "./Registration";

  export default {
    name: "Home",
    components: {
      Login,
      Registration,
    },
    data() {
      return {
        user: '',
        show: {
          register: false,
          login: false,
          shops: false,
          products: false,
          order_list: false,
          order: false,
        },
        snackbar: false,
        snackbar_message: '',
        timeout: 3000,
        progress: false,
        progress_timeout: 1100,
        open_drawer: true,
      }
    },
    created() {
      this.auth();
    },
    methods: {
      auth() {
        this.show.login = !sessionStorage.getItem('auth_token');
      },
      openColorSnackbar(snack_mes) {
        this.snackbar = true;
        this.snackbar_message = snack_mes;
        setTimeout(() => {
          this.snackbar = false;
        }, this.timeout);
      },
      openColorProgressbar() {
        this.progress = true;
      },
      closeColorProgressbar() {
        setTimeout(() => {
          this.progress = false;
        }, this.progress_timeout);
      },
      logout() {
        sessionStorage.removeItem('auth_token');
        window.location = '/';
      },
      goMain() {
        this.show.login = false;
        this.show.register = false;
        this.show.order_list = true;
      },
      goRegistration() {
        this.show.login = false;
        this.show.register = true;
      },
      goShopList() {
        this.show.shops = true;
        this.show.products = false;
        this.show.order_list = false;
        this.show.order = false;
      },
      goProductList() {
        this.show.products = true;
        this.show.shops = false;
        this.show.order_list = false;
        this.show.order = false;
      },
      goOrderList() {
        this.show.order_list = true;
        this.show.shops = false;
        this.show.products = false;
        this.show.order = false;
      },
      goOrder(order_num) {
        this.order_num = order_num;
        this.show.order = true;
        this.show.order_list = false;
        this.show.shops = false;
        this.show.products = false;
      },
    }
  }
</script>

<style scoped>
  .app-progress {
    padding-top: 3px;
  }

  .draw-move {
    transition: all .25s;
    margin-left: 256px;
  }
  .draw-return {
    transition: all .25s;
    margin-left: 0;
  }
  .app-move{
    transition: all .25s;
    margin-right: 256px;
  }
  .app-return{
    transition: all .25s;
    margin-right: 0px;
  }

</style>
