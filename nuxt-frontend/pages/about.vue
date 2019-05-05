<template>
  <div class="about-container">
    <div class="content">
      <div class="header-image">
        <img class="img-main" src="@/assets/images/abouthero.jpg" />
      </div>
      <div class="header">
        <h1 class="page-title">About Paperwiff</h1>
        <p class="desc">
          A platform for Readers and Writers to express and interact in
          vernacular languages.
        </p>
      </div>
      <v-container>
        <div class="main">
          <div class="intro-main">
            <p class="content-text">
              Founded in 2018, Paperwiff is a NSRCEL, IIM-B pre-incubated
              start-up which provides an end-to- end content solution with
              enhanced digital marketing techniques. Content moderation and
              content strategies are very well taken care by Paperwiff.
              Paperwiff is a next generation content curator and marketing lead
              in the content industry.
            </p>
          </div>

          <div class="cards-main">
            <div class="about-card">
              <div class="card-title">
                <v-icon large color="green darken-2">fas fa-campground</v-icon>
                <h3 class="subheader-text">Misson</h3>
              </div>
              <p class="content-text">
                Paperwiff encompasses the mission of inviting more and more
                writers and readers to walk on-board on the digital landscape of
                content world.
              </p>
              <p class="content-text">
                Paperwiff is exponentially changing the traditional methods of
                writing and its reach till the end user using advanced
                technologies of Machine Learning and Artificial Intelligence.
              </p>
              <p class="content-text">
                By 2021, Paperwiff plans to revive the dead vernacular languages
                across the globe, making every person and every language count.
              </p>
            </div>
            <div class="about-card">
              <div class="card-title">
                <v-icon large color="orange lighten-3"
                  >fab fa-first-order</v-icon
                >

                <h3 class="subheader-text">Vision</h3>
              </div>
              <p class="content-text">
                The vision of Paperwiff is to give freedom of expression to the
                global demography with the confidence of writing, anytime and
                anywhere, in any vernacular languages. Paperwiff is a barrier
                breaker to all the technical and marketing hassles of the
                content industry.
              </p>
            </div>
            <div class="about-card">
              <div class="card-title">
                <v-icon large color="red accent-2">fas fa-walking</v-icon>
                <h3 class="subheader-text">Philosopy</h3>
              </div>
              <p class="content-text">
                At Paperwiff we take pride that our company was formed with one
                premise in mind, and that is to bring a degree of experience,
                dedication, and professionalism to the writing industry that has
                long been missing. We aspire to be ahead of the competition when
                quality and performance are evaluated. Paperwiff will work
                continuously to bring in new ideas, to give our clients the
                latest in creative content industry.
              </p>
              <p class="content-text">
                The platform was created in 2019. The Twitter account,
                @paperwiff was around before then. We are based out of Bangalore
                City
              </p>
            </div>
          </div>
        </div>
      </v-container>
    </div>
  </div>
</template>

<script>
export default {}
</script>
<style lang="scss">
.about-container {
  .header-image {
    max-height: 400px;
    overflow: hidden;
    .img-main {
      width: 100%;
      height: 400px;
      object-fit: cover;
    }
  }
  .header {
    width: 100%;
    background: #fff;
    box-sizing: border-box;
    padding: 25px 20px;
    text-align: center;
    box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.05);
    .page-title {
      color: #2e2e2e;
      box-sizing: border-box;
      padding: 5px 0;
    }
    .desc {
      font-size: 15px;
      line-height: 2;
      color: #6e6e6e;
    }
  }
  .main {
    max-width: 1200px;
    margin: auto;
    .intro-main {
      background: #fff;

      box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.05);
      box-sizing: border-box;
      padding: 20px;

      border-radius: 8px;

      .content-text {
        box-sizing: border-box;
        padding: 20px 0;
        font-weight: normal;
        color: #6e6e6e;
        font-size: 18px;
        line-height: 2;
        text-align: center;
      }
    }
    .cards-main {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-evenly;
      padding: 20px 0;
      box-sizing: border-box;
      .about-card {
        flex-basis: 30%;

        background: #fff;

        box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.05);
        box-sizing: border-box;
        padding: 20px;

        border-radius: 8px;
        margin: 0 10px;

        cursor: pointer;
        @media (max-width: 768px) {
          flex-basis: 100%;
          margin-bottom: 20px;
        }
        transition: all 0.4s ease-in-out;
        &:nth-child(1) {
          border-bottom: 5px solid #388e3c;
        }
        &:nth-child(2) {
          border-bottom: 5px solid #ffcc80;
        }
        &:nth-child(3) {
          border-bottom: 5px solid #ff5252;
        }
        &:hover {
          .card-title {
            .v-icon {
              font-size: 50px !important;
            }
          }
        }
        .card-title {
          display: inline-flex;
          align-items: center;
        }
        .subheader-text {
          box-sizing: border-box;
          padding: 20px 0;
          text-transform: capitalize;
          font-weight: normal;
          color: #2e2e2e;
          font-size: 25px;
          padding-left: 20px;
        }
        .content-text {
          font-size: 15px;
          line-height: 2;
          color: #6e6e6e;
        }
      }
    }
  }
}
</style>
