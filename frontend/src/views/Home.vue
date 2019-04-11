<template>
  <div class="home">
    <div class="logo-section">
      <header>
        <h3 class="display-4">PaperWiff</h3>
        <blockquote
          class="blockquote"
        >Lorem ipsum dolor sit amet, consectetur adipisicing elit. Harum maiores modi quidem veniam, expedita quis laboriosam, ullam facere adipisci, iusto, voluptate sapiente corrupti asperiores rem nemo numquam fuga ab at.</blockquote>
      </header>
    </div>
    <!-- <div class="main-slider">
      <v-carousel hide-controls hide-delimiters>
        <v-carousel-item v-for="(item,i) in items" :key="i" :src="item.src"></v-carousel-item>
      </v-carousel>
    </div>-->

    <div class="main-content">
      <v-layout>
        <v-flex xs4>
          <div class="user-in">
            <v-avatar>
              <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John">
            </v-avatar>
            <p>Navaneeth</p>
          </div>
          <div class="tags-main">
            <header>Tags</header>
            <div class="chip-content">
              <v-chip v-model="chip1" close>#Closable</v-chip>

              <v-chip v-model="chip2" close>#Remove</v-chip>

              <v-chip v-model="chip3" close>#Success</v-chip>

              <v-chip v-model="chip4" close>#Complete</v-chip>
            </div>
          </div>
        </v-flex>
        <v-flex xs8>
          <div class="articles-tab">
            <v-tabs centered color="#f2f2f2" icons-and-text>
              <v-tabs-slider color="black"></v-tabs-slider>

              <v-tab href="#tab-1">Feed</v-tab>

              <v-tab href="#tab-2">Popular</v-tab>

              <v-tab href="#tab-3">Latest</v-tab>

              <v-tab-item v-for="i in 3" :key="i" :value="'tab-' + i">
                <v-card flat>
                  <v-container fluid grid-list-md>
                    <v-layout row wrap>
                      <v-flex
                        v-for="card in cards"
                        :key="card.title"
                        v-bind="{ [`xs${card.flex}`]: true }"
                      >
                        <v-card>
                          <v-img :src="card.src" height="200px">
                            <v-container fill-height fluid pa-2>
                              <v-layout fill-height>
                                <v-flex xs12 align-end flexbox>
                                  <span class="headline white--text" v-text="card.title"></span>
                                </v-flex>
                              </v-layout>
                            </v-container>
                          </v-img>

                          <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn icon>
                              <v-icon>favorite</v-icon>
                            </v-btn>
                            <v-btn icon>
                              <v-icon>bookmark</v-icon>
                            </v-btn>
                            <v-btn icon>
                              <v-icon>share</v-icon>
                            </v-btn>
                          </v-card-actions>
                        </v-card>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-card>
              </v-tab-item>
            </v-tabs>
          </div>
        </v-flex>
      </v-layout>
    </div>
  </div>
</template>
<script>
export default {
  name: "Home",
  data() {
    return {
      items: [
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg"
        },
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/sky.jpg"
        },
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/bird.jpg"
        },
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/planet.jpg"
        }
      ],
      cards: [
        {
          title: "Pre-fab homes",
          src: "https://cdn.vuetifyjs.com/images/cards/house.jpg",
          flex: 5
        },
        {
          title: "Favorite road trips",
          src: "https://cdn.vuetifyjs.com/images/cards/road.jpg",
          flex: 4
        },
        {
          title: "Best airlines",
          src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
          flex: 3
        }
      ]
    };
  }
};
</script>
